import pytest

from leet_code.int_to_roman import int_to_roman


@pytest.mark.parametrize(
    "input_num, expected_output",
    [
        (1, "I"),
        (4, "IV"),
        (9, "IX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (3999, "MMMCMXCIX"),
        (0, ""),  # Edge case: 0 is not a valid input for Roman numerals
        (4000, ""),  # Edge case: 4000 is not a valid input for Roman numerals
    ],
)
def test_int_to_roman(input_num: int, expected_output: str) -> None:
    """Test the int_to_roman function."""
    if input_num in [0, 4000]:
        with pytest.raises(ValueError):
            int_to_roman(input_num)
    else:
        result = int_to_roman(input_num)
        assert result == expected_output, f"Expected {expected_output}, but got {result}"
        print(f"Test passed for input {input_num}: {result} == {expected_output}")
