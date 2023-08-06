from typing import Optional
import logging

from rdkit import Chem as rdkit_Chem
from rdkit.rdBase import BlockLogs as rdkit_BlockLogs

from orderly.types import *

LOG = logging.getLogger(__name__)


def remove_mapping_info_and_canonicalise_smiles(
    molecule_identifier: MOLECULE_IDENTIFIER,
) -> Optional[SMILES]:
    """
    Strips away mapping info and returns canonicalised SMILES.
    """
    # This function can handle smiles both with and without mapping info
    _ = rdkit_BlockLogs()
    # remove mapping info and canonicalsie the molecule_identifier at the same time
    # converting to mol and back canonicalises the molecule_identifier string
    try:
        m = rdkit_Chem.MolFromSmiles(molecule_identifier)
        for atom in m.GetAtoms():
            atom.SetAtomMapNum(0)
        return str(rdkit_Chem.MolToSmiles(m))
    except AttributeError:
        return None


def canonicalise_smiles(
    molecule_identifier: MOLECULE_IDENTIFIER,
) -> Optional[SMILES]:
    """
    Returns canonicalised SMILES, ignoring mapping info (ie if mapping info is present, it will be retained)
    """
    _ = rdkit_BlockLogs()
    # remove mapping info and canonicalsie the molecule_identifier at the same time
    # converting to mol and back canonicalises the molecule_identifier string
    try:
        return str(rdkit_Chem.CanonSmiles(molecule_identifier))
    except AttributeError:
        return None
    except Exception as e:
        # raise e
        return None


def get_canonicalised_smiles(
    molecule_identifier: MOLECULE_IDENTIFIER, is_mapped: bool = False
) -> Optional[SMILES]:
    """
    Returns canonicalised SMILES, stripping mapping info if is_mapped is True.
    Removing mapping info and then canonicalising is slower than just canonicalising, so we only attempt to remove mapping if mapping info is present.
    """
    # attempts to remove mapping info and canonicalise a smiles string and if it fails, returns the name whilst adding to a list of non smiles names
    # molecule_identifier: string, that is a smiles or an english name of the molecule
    if is_mapped:
        attempted_canon_smiles = remove_mapping_info_and_canonicalise_smiles(
            molecule_identifier
        )
    else:
        attempted_canon_smiles = canonicalise_smiles(molecule_identifier)
    if attempted_canon_smiles is not None:
        return attempted_canon_smiles
    else:
        if molecule_identifier[0] == "[":
            if molecule_identifier[-1] == "]":
                return canonicalise_smiles(molecule_identifier[1:-1])
        else:
            return canonicalise_smiles(f"[{molecule_identifier}]")
        return None
