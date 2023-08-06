import os
import sys
import pathlib
import logging

LOG = logging.getLogger(__name__)


def _get_orderly_data_path() -> pathlib.Path:
    file_path = sys.modules["orderly.data"].__file__
    if file_path is None:
        e = ValueError("The path for orderly.data was not found")
        LOG.error(e)
        raise e
    return pathlib.Path(os.path.dirname(file_path))


def get_path_of_test_ords() -> pathlib.Path:
    return _get_orderly_data_path() / "test_data" / "ord_test_data"


def get_path_of_test_extracted_ords(trust_labelling: bool = False) -> pathlib.Path:
    trust_labelling_str = (
        "_trust_labelling" if trust_labelling else "_dont_trust_labelling"
    )
    return (
        _get_orderly_data_path()
        / "test_data"
        / f"extracted_ord_test_data{trust_labelling_str}"
    )


def get_path_of_molecule_names(trust_labelling: bool = False) -> pathlib.Path:
    trust_labelling_str = (
        "_trust_labelling" if trust_labelling else "_dont_trust_labelling"
    )
    return (
        _get_orderly_data_path()
        / "test_data"
        / f"extracted_ord_test_data{trust_labelling_str}"
        / "molecule_names"
    )
