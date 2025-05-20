import pytest

from leet_code.int_to_roman import int_to_roman, roman_to_int


@pytest.mark.parametrize(
    ("input_num", "expected_output"),
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
        with pytest.raises(ValueError, match="Input must be between 1 and 3999."):
            int_to_roman(input_num)
    else:
        result = int_to_roman(input_num)
        assert result == expected_output, f"Expected {expected_output}, but got {result}"
        print(f"Test passed for input {input_num}: {result} == {expected_output}")


# Test cases for the roman_to_int function
@pytest.mark.parametrize(
    ("input_roman", "expected_output"),
    [
        ("I", 1),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("MMMCMXCIX", 3999),
        ("", 0),  # Edge case: empty string
        ("MMMM", 4000),  # Edge case: invalid Roman numeral
    ],
)
def test_roman_to_int(input_roman: str, expected_output: int) -> None:
    """Test the roman_to_int function."""
    if input_roman in {"MMMM", ""}:
        with pytest.raises(ValueError):  # noqa: PT011
            roman_to_int(input_roman)

    else:
        result = roman_to_int(input_roman)
        assert result == expected_output, f"Expected {expected_output}, but got {result}"
        print(f"Test passed for input {input_roman}: {result} == {expected_output}")
