import pytest
from roman_numeral import roman_to_number


@pytest.mark.parametrize("input_data,expected", [
    ("MXVII", 1017),
    ("VI", 6),
    ("X", 10),
    ("XVI", 16),
    ("CXV", 115),
    ("RER", None)

])
def test_roman_numeral(input_data, expected):
    assert roman_to_number(input_data) == expected
