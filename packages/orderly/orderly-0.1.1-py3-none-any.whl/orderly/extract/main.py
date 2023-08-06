import logging
from typing import List, Dict, Tuple, Set, Optional
import datetime
import pathlib
import click
import json

from click_loglevel import LogLevel

import pandas as pd
import tqdm
import tqdm.contrib.logging

from rdkit import Chem as rdkit_Chem
from rdkit.rdBase import BlockLogs as rdkit_BlockLogs

import orderly.extract.extractor
import orderly.extract.canonicalise
import orderly.extract.defaults
import orderly.data.solvents

from orderly.types import *

LOG = logging.getLogger(__name__)

import orderly.data.util


def get_file_names(
    directory: pathlib.Path,
    file_ending: str = ".pb.gz",
    include_cleaned_USPTO_file: bool = False,
) -> List[pathlib.Path]:
    """
    Goes into the ord data directory and for each folder extracts the file path of all sub data files with the file ending

    The reason for include_cleaned_USPTO_file:
        This file: ord_dataset-de0979205c84441190feef587fef8d6d is a cleaned version of USPTO from https://pubs.rsc.org/en/content/articlelanding/2019/SC/C8SC04228D

        So it doesn't include new information, and extraction from this file is pretty slow because it's 10x bigger than the second largest dataset in ORD (400k reactions vs 40k). So default behaviour is to ignore it.
    """

    files = []
    for i in directory.glob("./*"):
        for j in i.glob(f"./*{file_ending}"):
            if "ord_dataset-de0979205c84441190feef587fef8d6d" not in str(j):
                files.append(j)
            elif include_cleaned_USPTO_file:
                files.append(j)

    return sorted(
        files
    )  # sort just so that there is no randomness in order of processing


def merge_mol_names(
    molecule_names_path: pathlib.Path = pathlib.Path("data/orderly/molecule_names"),
    output_file_path: pathlib.Path = pathlib.Path(
        "data/orderly/all_molecule_names.csv"
    ),
    overwrite: bool = True,
    molecule_names_file_ending: str = ".csv",
) -> None:
    """
    Merges all the files containing molecule non-smiles identifiers (typically english names) into one file.
    """
    if output_file_path.suffix != ".csv":
        suffix_error = ValueError(
            f"The file extension for {output_file_path=} is expected to be .csv not {output_file_path.suffix}"
        )
        LOG.error(suffix_error)
        raise suffix_error
    output_file_path.parent.mkdir(parents=True, exist_ok=True)

    if not overwrite:
        if output_file_path.exists():
            file_error = FileExistsError(
                f"{output_file_path} exists, with {overwrite=}, we expect the file to not exist."
            )
            LOG.error(file_error)
            raise file_error

    full_lst = []
    for f in molecule_names_path.glob(f"./*{molecule_names_file_ending}"):
        full_lst += orderly.data.util.load_list(f)

    unique_molecule_names = sorted(list(set(full_lst)))

    # save the list
    orderly.data.util.save_list(x=unique_molecule_names, path=output_file_path)
    LOG.info(f"Saved list of unique molecule names at {output_file_path=}")


def build_solvents_set_and_dict(
    solvents_path: Optional[pathlib.Path] = None,
) -> Tuple[Set[CANON_SMILES], Dict[MOLECULE_IDENTIFIER, CANON_SMILES]]:
    """
    Builds a set of canonical smiles strings for all solvents (used to identify which agents are solvents) and a dictionary of solvent names to canonical smiles strings (for name resolution)
    """
    solvents = orderly.data.solvents.get_solvents(path=solvents_path)

    solvents["canonical_smiles"] = solvents["smiles"].apply(
        orderly.extract.canonicalise.get_canonicalised_smiles
    )

    # TODO raise error if any of the canonical smiles have a none in

    solvents_set = set(solvents["canonical_smiles"])

    # Combine the lists into a sequence of key-value pairs
    key_value_pairs = zip(
        list(solvents["solvent_name_1"])
        + list(solvents["solvent_name_2"])
        + list(solvents["solvent_name_3"]),
        list(solvents["canonical_smiles"])
        + list(solvents["canonical_smiles"] + list(solvents["canonical_smiles"])),
    )

    # Create a dictionary from the sequence
    solvents_dict = dict(key_value_pairs)

    return solvents_set, solvents_dict


def build_replacements(
    molecule_replacements: Optional[Dict[MOLECULE_IDENTIFIER, SMILES]] = None,
    molecule_str_force_nones: Optional[List[INVALID_IDENTIFIER]] = None,
) -> Dict[MOLECULE_IDENTIFIER | INVALID_IDENTIFIER, Optional[SMILES]]:
    """
    Builds dictionary mapping english name molecule identifiers to canonical smiles. Dict is based on manually curated list.
    """
    _ = rdkit_BlockLogs()  # removes excessive warnings

    if molecule_replacements is None:
        molecule_replacements = orderly.extract.defaults.get_molecule_replacements()

    # Iterate over the dictionary and canonicalize each SMILES string
    for key, value in molecule_replacements.items():
        mol = rdkit_Chem.MolFromSmiles(value)
        if mol is not None:
            molecule_replacements[key] = rdkit_Chem.MolToSmiles(mol)

    if molecule_str_force_nones is None:
        molecule_str_force_nones = (
            orderly.extract.defaults.get_molecule_str_force_nones()
        )

    molecule_replacements_with_force_nones: Dict[MOLECULE_IDENTIFIER | INVALID_IDENTIFIER, Optional[SMILES]] = molecule_replacements.copy()  # type: ignore

    for molecule_str in molecule_str_force_nones:
        molecule_replacements_with_force_nones[molecule_str] = None

    LOG.debug("Got molecule replacements")
    return molecule_replacements_with_force_nones


def get_manual_replacements_dict(
    molecule_replacements: Optional[Dict[MOLECULE_IDENTIFIER, CANON_SMILES]] = None,
    molecule_str_force_nones: Optional[List[MOLECULE_IDENTIFIER]] = None,
    solvents_path: Optional[pathlib.Path] = None,
) -> MANUAL_REPLACEMENTS_DICT:
    """
    Combines manually curated dictioary of molecule names to canonical smiles strings with the dictionary of solvent names to canonical smiles strings.
    """
    manual_replacements_dict = build_replacements(
        molecule_replacements=molecule_replacements,
        molecule_str_force_nones=molecule_str_force_nones,
    )
    solvents_dict = orderly.data.solvents.get_solvents_dict(path=solvents_path)
    manual_replacements_dict.update(solvents_dict)
    return manual_replacements_dict


def extract(
    output_path: pathlib.Path,
    file: pathlib.Path,
    trust_labelling: bool,
    consider_molecule_names: bool,
    manual_replacements_dict: MANUAL_REPLACEMENTS_DICT,
    solvents_set: Set[CANON_SMILES],
    extracted_ord_data_folder: str = "extracted_ords",
    molecule_names_folder: str = "molecule_names",
    name_contains_substring: Optional[str] = None,
    inverse_substring: bool = False,
    overwrite: bool = True,
) -> None:
    """
    Extract information from an ORD file.
    """
    LOG.debug(f"Attempting extraction for {file}")
    instance = orderly.extract.extractor.OrdExtractor(
        ord_file_path=file,
        trust_labelling=trust_labelling,
        consider_molecule_names=consider_molecule_names,
        manual_replacements_dict=manual_replacements_dict,
        solvents_set=solvents_set,
        contains_substring=name_contains_substring,
        inverse_contains_substring=inverse_substring,
    )
    if instance.full_df is None:
        LOG.debug(f"Skipping extraction for {file}")
        return

    filename = instance.filename
    LOG.info(f"Completed extraction for {file}: {filename}")

    df_path = output_path / extracted_ord_data_folder / f"{filename}.parquet"
    molecule_names_path = (
        output_path / molecule_names_folder / f"molecules_{filename}.csv"
    )
    if not overwrite:
        if df_path.exists():
            e = FileExistsError(
                f"Trying to overwrite {df_path} which exists, overwrite must be true to do this"
            )
            LOG.error(e)
            raise e
        if molecule_names_path.exists():
            e = FileExistsError(
                f"Trying to overwrite {molecule_names_path} which exists, overwrite must be true to do this"
            )
            LOG.error(e)
            raise e

    instance.full_df.to_parquet(df_path)

    LOG.debug(f"Saved df at {df_path}")

    # list of the names used for molecules, as opposed to SMILES strings
    # save the non_smiles_names_list to file

    assert (
        instance.non_smiles_names_list is not None
    ), "we dont expect this to be none here"
    orderly.data.util.save_list(
        x=instance.non_smiles_names_list, path=molecule_names_path
    )
    LOG.debug(f"Saves molecule names for {filename} at {molecule_names_path}")


@click.command()
@click.option(
    "--data_path",
    type=str,
    default="data/ord/",
    show_default=True,
    help="The path of the folder that contains the ORD data",
)
@click.option(
    "--ord_file_ending",
    type=str,
    default=".pb.gz",
    help="The file ending for the ord data, if empty will extract all files in the folder",
    show_default=True,
)
@click.option(
    "--trust_labelling",
    type=bool,
    default=False,
    show_default=False,
    help="""
- If True, maintain the labelling and ordering of the original data.
- If False: Trust the mapped reaction more than the labelled data. A reaction string should be of the form reactants>agents>products; however, agents (particularly reagents) may sometimes appear as reactants on the LHS, so any molecules on the LHS we re-label as a reagent if it (i) does not contain any atom mapped atoms, (ii) the molecule appears on both the LHS and RHS (ie it is unreacted). Note that the original labelling is trusted (by default) if the reaction is not mapped. The agents list consists of catalysts, reagents and solvents; any molecules that occur in the set of solvents are extracted from the agents list and re-labelled as solvents, while the remaining molecules remain labelled as agents. Then the list of agents and solvents is sorted alphabetically, and finally any molecules that contain a transition metal were moved to the front of the agents list; ideally these lists be sorted by using chemical reasoning (e.g. by amount or importance), however this information doesn't exist, so we sort alphabetically and move transition metal containing molecules to the front (since its likely to be a catalyst) to at least add some order, albeit an arbitrary one. Prior work indicates that sequential prediction of conditions (with the caatlyst first) outperforms predicting all conditions in a single output layer (https://doi.org/10.1021/acscentsci.8b00357), so ordering may be helpful.""",
)
@click.option(
    "--consider_molecule_names",
    type=bool,
    default=False,
    show_default=True,
    help="Controls whether plain text names are extracted as a backup. Molecules stored in the ORD input/outcome field can be represented in a number of different ways, including SMILES, InChI, and a (plain English) name. The SMILES representation is always the preferred representation. This bool controls what happens if there's no SMILES string available: if consider_molecule_names=False, the input/outcome extractor simply returns None for that molecule; if consider_molecule_names=True, the input/outcome extractor will return the string to be added to the reaction, check whether the string is resolvable as SMILES (to canonicalise it), and if it is not resolvable, the string is added to the non_smiles_names_list to be handled/removed during cleaning.",
)
@click.option(
    "--output_path",
    type=str,
    default="data/orderly/",
    show_default=True,
    help="The path to the folder than will contain the extracted_ord_data_folder and molecule_names_folder",
)
@click.option(
    "--extracted_ord_data_folder",
    type=str,
    default="extracted_ords",
    show_default=True,
    help="The name of folder than contains the extracted ord dataframes",
)
@click.option(
    "--solvents_path",
    type=str,
    default="default",
    show_default=True,
    help="The path to the solvents csv, if None will use the default",
)
@click.option(
    "--molecule_names_folder",
    type=str,
    default="molecule_names",
    show_default=True,
    help="The name of the folder that contains the molecule_name per folder",
)
@click.option(
    "--merged_molecules_file",
    type=str,
    default="all_molecule_names.csv",
    show_default=True,
    help="The name and file tag of the merged_molecules file (the merged_molecules_file is outputed to output_path / merged_molecules_file)",
)
@click.option(
    "--use_multiprocessing",
    type=bool,
    default=True,
    show_default=True,
    help="Boolean to make the processing of each ORD file done with multiprocessing",
)
@click.option(
    "--name_contains_substring",
    type=str,
    default="uspto",
    show_default=True,
    help="A filter for the ORD file names, will only extract files that includes the str. If left empty will not search for anything. For example 'uspto' grabs only uspto data",
)
@click.option(
    "--inverse_substring",
    type=bool,
    default=False,
    show_default=True,
    help="Inversed the name contains substring, so name_contains_substring='uspto' & inverse_substring=True will exclude names with uspto in",
)
@click.option(
    "--overwrite",
    type=bool,
    default=False,
    show_default=True,
    help="If true, will overwrite existing files, else will through an error if a file exists",
)
@click.option(
    "--log_file",
    type=str,
    default="default_path_extract.log",
    show_default=True,
    help="path for the log file for extraction",
)
@click.option("--log-level", type=LogLevel(), default=logging.INFO)
def main_click(
    data_path: str,
    ord_file_ending: str,
    trust_labelling: bool,
    consider_molecule_names: bool,
    output_path: str,
    extracted_ord_data_folder: str,
    solvents_path: str,
    molecule_names_folder: str,
    merged_molecules_file: str,
    use_multiprocessing: bool,
    name_contains_substring: str,
    inverse_substring: bool,
    overwrite: bool,
    log_file: str,
    log_level: int,
) -> None:
    """
    After downloading the dataset from ORD, this script will extract the data and write it to file. During extraction we also extract unresolvable/uncanonicalisable molecules and keep a record of these and then remove them during cleaning
        Example:


    Args:

    1) data_path: str
        - Path to the folder that contains the ORD data
    2) ord_file_ending: str
        - the file ending of the ord data typically ".pb.gz"
    3) trust_labelling: Bool
        - If True, maintain the labelling and ordering of the original data.
        - If False: Trust the mapped reaction more than the labelled data. A reaction string should be of the form reactants>agents>products; however, agents (particularly reagents) may sometimes appear as reactants on the LHS, so any molecules on the LHS we re-label as a reagent if it (i) does not contain any atom mapped atoms, (ii) the molecule appears on both the LHS and RHS (ie it is unreacted). Note that the original labelling is trusted (by default) if the reaction is not mapped. The agents list consists of catalysts, reagents and solvents; any molecules that occur in the set of solvents are extracted from the agents list and re-labelled as solvents, while the remaining molecules remain labelled as agents. Then the list of agents and solvents is sorted alphabetically, and finally any molecules that contain a transition metal were moved to the front of the agents list; ideally these lists be sorted by using chemical reasoning (e.g. by amount or importance), however this information doesn't exist, so we sort alphabetically and move transition metal containing molecules to the front (since its likely to be a catalyst) to at least add some order, albeit an arbitrary one. Prior work indicates that sequential prediction of conditions (with the catalyst first) outperforms predicting all conditions in a single output layer (https://doi.org/10.1021/acscentsci.8b00357), so ordering may be helpful.
    3) consider_molecule_names: bool
    4) output_path: str
        - The path to the folder than will contain the extracted_ord_data_folder and molecule_names_folder
    5) extracted_ord_data_folder: str
        - The name of folder than contains the extracted ord dataframes
    6) solvents_path: Optional[str]
        - The path to the solvents csv, if None will use the default
    7) molecule_names_folder: str
        - The name of the folder that contains the molecule_name per folder
    8) merged_molecules_file: str
        - The name and file tag of the merged_molecules file (the merged_molecules_file is outputed to output_path / merged_molecules_file)
    9) use_multiprocessing: bool
        - Boolean to make the processing of each ORD file done with multiprocessing
    10) name_contains_substring: Optional[str]
        - A filter for the ORD file names, will only extract files that includes the str. If left empty will not search for anything. For example 'uspto' grabs only uspto data (https://figshare.com/articles/dataset/Chemical_reactions_from_US_patents_1976-Sep2016_/5104873)
    11) inverse_substring: bool
        - Inversed the name contains substring, so name_contains_substring='uspto' & inverse_substring=True will exclude names with uspto in
    12) overwrite: bool
        - If true, will overwrite existing files, else will through an error if a file exists.


    Functionality:

    1) Data extracted from ORD comes in a large number of files (.pd.gz) batched in a large number of sub-folders. First step is to extract all filepaths that contain data of interest (e.g. everything if name_contains_substring is empty or only uspto data if name_contains_substring='uspto').
    2) Iteration over all filepaths to extract the following data:
        - The mapped reaction (unchanged)
        - Reactants, products, and agents (reagents, solvents and catalysts)
            - NB: If trust_labelling=True this info is extracted from .input and .outcomes labelling. If trust_labelling=False (default) it is extracted from the mapped reaction string & mapping is considered to reason on whether a molecule is a reactant, solvent, or agent.
        - Temperature: All temperatures were converted to Celcius. If only the control type was specified, the following mapping was used: 'AMBIENT' -> 25, 'ICE_BATH' -> 0, 'DRY_ICE' -> -78.5, 'LIQUID_NITROGEN' -> -196.
        - Time: All times were converted to hours.
        - Yield (for each product): The PERCENTAGEYIELD was preferred, but if this was not available, the CALCULATEDPERCENTYIELD was used instead. If neither was available, the value was set to None.
        - Procedure_details: Plain text string describing the procedure in English.
    3) Canonicalisation and light cleaning
        - All SMILES strings were canonicalised using RDKit.
        - A "replacements dictionary" was created to replace common names with their corresponding SMILES strings. This dictionary was created by iterating over the most common names in the dataset and replacing them with their corresponding SMILES strings. This was done semi-manually, with some dictionary entries coming from solvents.csv and others being added within the script (in the build_replacements function; mainly concerning catalysts).
        - The final light cleaning step depends on the value of trust_labelling (see above, in the Args section).
        - Reactions will only be added if the reactants and products are different (i.e. no crystalisation reactions etc.)
    4) Build a pandas DataFrame from this data (one for each ORD file), and save each as a file
    5) Create a list of all molecule names and save as a file. This comes in handy when performing name resolution (many molecules are represented with an english name as opposed to a smiles string). A molecule is understood as having an english name (as opposed to a SMILES string) if it is unresolvable by RDKit.
    6) Merge all the lists of molecule names to create a list of unique molecule names (in merged_molecules_file eg "data/ORD/all_molecule_names.csv").

    Output:

    1) A file with the cleaned data for each folder of data. NB: Temp always in C, time always in hours
    2) A list of all unique molecule names (in merged_molecules_file)
    """

    _solvents_path: Optional[pathlib.Path] = None
    if solvents_path != "default":
        _solvents_path = pathlib.Path(solvents_path)

    _name_contains_substring: Optional[str] = None
    if name_contains_substring != "":
        _name_contains_substring = name_contains_substring

    file_name = pathlib.Path(output_path).name
    _log_file = pathlib.Path(output_path) / f"{file_name}_extract.log"
    if log_file != "default_path_extract.log":
        _log_file = pathlib.Path(log_file)

    main(
        data_path=pathlib.Path(data_path),
        ord_file_ending=ord_file_ending,
        trust_labelling=trust_labelling,
        consider_molecule_names=consider_molecule_names,
        output_path=pathlib.Path(output_path),
        extracted_ord_data_folder=extracted_ord_data_folder,
        solvents_path=_solvents_path,
        molecule_names_folder=molecule_names_folder,
        merged_molecules_file=merged_molecules_file,
        use_multiprocessing=use_multiprocessing,
        name_contains_substring=_name_contains_substring,
        inverse_substring=inverse_substring,
        overwrite=overwrite,
        log_file=_log_file,
        log_level=log_level,
    )


def main(
    data_path: pathlib.Path,
    ord_file_ending: str,
    trust_labelling: bool,
    consider_molecule_names: bool,
    output_path: pathlib.Path,
    extracted_ord_data_folder: str,
    solvents_path: Optional[pathlib.Path],
    molecule_names_folder: str,
    merged_molecules_file: str,
    use_multiprocessing: bool,
    name_contains_substring: Optional[str],
    inverse_substring: bool,
    overwrite: bool,
    log_file: pathlib.Path = pathlib.Path("extraction.log"),
    log_level: int = logging.INFO,
) -> None:
    """
    After downloading the dataset from ORD, this script will extract the data and write it to files.
        Example:


    Args:

    1) data_path: str
        - Path to the folder that contains the ORD data
    2) ord_file_ending: str
        - the file ending of the ord data typically ".pb.gz"
    3) trust_labelling: Bool
        - If True, maintain the labelling and ordering of the original data.
        - If False: Trust the mapped reaction more than the labelled data. A reaction string should be of the form reactants>agents>products; however, agents (particularly reagents) may sometimes appear as reactants on the LHS, so any molecules on the LHS we re-label as a reagent if it (i) does not contain any atom mapped atoms, (ii) the molecule appears on both the LHS and RHS (ie it is unreacted). Note that the original labelling is trusted (by default) if the reaction is not mapped. The agents list consists of catalysts, reagents and solvents; any molecules that occur in the set of solvents are extracted from the agents list and re-labelled as solvents, while the remaining molecules remain labelled as agents. Then the list of agents and solvents is sorted alphabetically, and finally any molecules that contain a transition metal were moved to the front of the agents list; ideally these lists be sorted by using chemical reasoning (e.g. by amount or importance), however this information doesn't exist, so we sort alphabetically and move transition metal containing molecules to the front (since its likely to be a catalyst) to at least add some order, albeit an arbitrary one. Prior work indicates that sequential prediction of conditions (with the caatlyst first) outperforms predicting all conditions in a single output layer (https://doi.org/10.1021/acscentsci.8b00357), so ordering may be helpful.
    3) consider_molecule_names: bool
    4) output_path: pathlib.Path
        - The path to the folder than will contain the extracted_ord_data_folder and molecule_names_folder
    5) extracted_ord_data_folder: str
        - The name of folder than contains the extracted dataframes
    6) solvents_path: Optional[str]
        - The path to the solvents csv, if None will use the default
    7) molecule_names_folder: str
        - The name of the folder that contains the molecule_name per folder
    8) merged_molecules_file: str
        - The name and file tag of the merged_molecules file (the merged_molecules_file is outputed to output_path / merged_molecules_file)
    9) use_multiprocessing: bool
        - Boolean to make the processing of each ORD file done with multiprocessing
    10) name_contains_substring: Optional[str]
        - A filter for the ORD file names, will only extract files that includes the str. If left empty will not search for anything. For example 'uspto' grabs only uspto data (https://figshare.com/articles/dataset/Chemical_reactions_from_US_patents_1976-Sep2016_/5104873)
    11) inverse_substring: bool
        - Inversed the name contains substring, so name_contains_substring='uspto' & inverse_substring=True will exclude names with uspto in
    12) overwrite: bool
        - If true, will overwrite existing files, else will through an error if a file exists.


    Functionality:

    1) Data extracted from ORD comes in a large number of files (.pd.gz) batched in a large number of sub-folders. First step is to extract all filepaths that contain data of interest (e.g. everything if name_contains_substring is empty or only uspto data if name_contains_substring='uspto').
    2) Iteration over all filepaths to extract the following data:
        - The mapped reaction (unchanged)
        - Reactants, products, and agents (reagents, solvents and catalysts)
            - NB: If trust_labelling=True this info is extracted from .input and .outcomes labelling. If trust_labelling=False (default) it is extracted from the mapped reaction string & mapping is considered to reason on whether a molecule is a reactant, solvent, or agent.
        - Temperature: All temperatures were converted to Celcius. If only the control type was specified, the following mapping was used: 'AMBIENT' -> 25, 'ICE_BATH' -> 0, 'DRY_ICE' -> -78.5, 'LIQUID_NITROGEN' -> -196.
        - Time: All times were converted to hours.
        - Yield (for each product): The PERCENTAGEYIELD was preferred, but if this was not available, the CALCULATEDPERCENTYIELD was used instead. If neither was available, the value was set to None.
        - Procedure_details: Plain text string describing the procedure in English.
    3) Canonicalisation and light cleaning
        - All SMILES strings were canonicalised using RDKit.
        - A "replacements dictionary" was created to replace common names with their corresponding SMILES strings. This dictionary was created by iterating over the most common names in the dataset and replacing them with their corresponding SMILES strings. This was done semi-manually, with some dictionary entries coming from solvents.csv and others being added within the script (in the build_replacements function; mainly concerning catalysts).
        - The final light cleaning step depends on the value of trust_labelling (see above, in the Args section).
        - Reactions will only be added if the reactants and products are different (i.e. no crystalisation reactions etc.)
    4) Build a pandas DataFrame from this data (one for each ORD file), and save each as a file
    5) Create a list of all molecule names and save as a file. This comes in handy when performing name resolution (many molecules are represented with an english name as opposed to a smiles string). A molecule is understood as having an english name (as opposed to a SMILES string) if it is unresolvable by RDKit.
    6) Merge all the lists of molecule names to create a list of unique molecule names (in merged_molecules_file eg "data/ORD/all_molecule_names.csv").

    Output:

    1) A file with the cleaned data for each folder of data. NB: Temp always in C, time always in hours
    2) A list of all unique molecule names (in merged_molecules_file)
    """

    log_file.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        encoding="utf-8",
        format="%(name)s - %(levelname)s - %(asctime)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        level=log_level,
    )

    if not isinstance(data_path, pathlib.Path):
        e = ValueError(f"Expect pathlib.Path: got {type(data_path)}")
        LOG.error(e)
        raise e
    if not isinstance(output_path, pathlib.Path):
        e = ValueError(f"Expect pathlib.Path: got {type(output_path)}")
        LOG.error(e)
        raise e
    if solvents_path is not None:
        if not isinstance(solvents_path, pathlib.Path):
            e = ValueError(f"Expect pathlib.Path: got {type(solvents_path)}")
            LOG.error(e)
            raise e
    if not isinstance(merged_molecules_file, str):
        e = ValueError(
            f"Expect str: got {type(merged_molecules_file)}. This is just the name of the file"
        )
        LOG.error(e)
        raise e
    if name_contains_substring is not None:
        if not isinstance(name_contains_substring, str):
            e = ValueError(f"Expect str: got {type(name_contains_substring)}")
            LOG.error(e)
            raise e

    LOG.info("starting extraction")
    start_time = datetime.datetime.now()

    extracted_ords_path = output_path / extracted_ord_data_folder
    molecule_name_path = output_path / molecule_names_folder

    extracted_ords_path.mkdir(parents=True, exist_ok=True)
    molecule_name_path.mkdir(parents=True, exist_ok=True)

    files = get_file_names(directory=data_path, file_ending=ord_file_ending)

    solvents_set = orderly.data.solvents.get_solvents_set(path=solvents_path)
    manual_replacements_dict = get_manual_replacements_dict(solvents_path=solvents_path)

    kwargs = {
        "output_path": output_path,
        "trust_labelling": trust_labelling,
        "consider_molecule_names": consider_molecule_names,
        "manual_replacements_dict": manual_replacements_dict,
        "solvents_set": solvents_set,
        "extracted_ord_data_folder": extracted_ord_data_folder,
        "molecule_names_folder": molecule_names_folder,
        "name_contains_substring": name_contains_substring,
        "inverse_substring": inverse_substring,
        "overwrite": overwrite,
    }

    config_path = output_path / "extract_config.json"
    if not overwrite:
        if config_path.exists():
            e = FileExistsError(
                f"You are trying to overwrite the config file at {config_path} with {overwrite=}"
            )
            LOG.error(e)
            raise e
    copy_kwargs = kwargs.copy()
    copy_kwargs["output_path"] = str(copy_kwargs["output_path"])
    copy_kwargs["solvents_set"] = sorted(list(copy_kwargs["solvents_set"]))  # type: ignore

    with open(config_path, "w") as f:
        json.dump(copy_kwargs, f, indent=4, sort_keys=True)

    try:
        if use_multiprocessing:
            # somewhat dangerous imports so keeping localised
            import multiprocessing
            import joblib

            num_cores = multiprocessing.cpu_count()
            with tqdm.contrib.logging.logging_redirect_tqdm(loggers=[LOG]):
                joblib.Parallel(n_jobs=num_cores)(
                    joblib.delayed(extract)(file=file, **kwargs)
                    for file in tqdm.tqdm(files)
                )
        else:
            with tqdm.contrib.logging.logging_redirect_tqdm(loggers=[LOG]):
                for file in tqdm.tqdm(files):
                    extract(file=file, **kwargs)  # type: ignore
                    # mypy fails with kwargs
    except KeyboardInterrupt:
        LOG.info(
            "KeyboardInterrupt: exiting the extraction but will quickly merge the files"
        )
        pass

    merge_mol_names(
        molecule_names_path=molecule_name_path,
        output_file_path=output_path / merged_molecules_file,
        overwrite=overwrite,
        molecule_names_file_ending=".csv",
    )
    end_time = datetime.datetime.now()
    LOG.info("Duration: {}".format(end_time - start_time))
