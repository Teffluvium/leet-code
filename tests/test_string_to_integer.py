import pytest

from leet_code.string_to_integer import my_atoi


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("42", 42),
        ("   -42", -42),
        ("4193 with words", 4193),
        ("words and 987", 0),
        ("-91283472332", -2147483648),  # Underflow case
        ("91283472332", 2147483647),  # Overflow case
        ("", 0),
        ("   ", 0),
        ("+-2", 0),  # Invalid case
        ("-+2", 0),  # Invalid case
    ],
)
def test_my_atoi(input_str: str, expected: int) -> None:
    """
    Test the my_atoi function with various inputs.

    :param input_str: Input string to convert
    :param expected: Expected integer result
    """
    result = my_atoi(input_str)
    assert result == expected, f"Expected {expected}, but got {result}"
