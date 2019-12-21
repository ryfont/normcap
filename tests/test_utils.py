"""Unit tests for utils functions."""

# Extras
import pytest

# Own
from normcap.common import utils
from normcap.common.data_model import NormcapData

# PyLint can't handle fixtures correctly. Ignore.
# pylint: disable=redefined-outer-name


@pytest.fixture(scope="session")
def test_data():
    """Create NormcapData instance for testing."""
    data = NormcapData()
    data.top = 0
    data.bottom = 10
    data.left = 0
    data.right = 20
    data.words = [
        {"line_num": 1, "block_num": 1, "par_num": 1, "text": "one"},
        {"line_num": 2, "block_num": 1, "par_num": 1, "text": "two"},
        {"line_num": 2, "block_num": 1, "par_num": 2, "text": "three"},
        {"line_num": 3, "block_num": 1, "par_num": 2, "text": "four"},
    ]
    return data


def test_log_dataclass(test_data):
    """Does output contains all available attributes?"""
    expected_strings = [k for k, v in vars(test_data).items()]
    output = utils.log_dataclass("Test output", test_data, return_string=True)
    assert all([s in output for s in expected_strings])
