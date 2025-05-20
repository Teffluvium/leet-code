import pytest

from leet_code.length_of_longest_substring import length_of_longest_substring


@pytest.mark.parametrize(
    ("input_string", "expected_length"),
    [
        ("", 0),
        ("a", 1),
        ("abcdef", 6),
        ("abcabcbb", 3),
        ("aaaaaa", 1),
        ("pwwkew", 3),
        ("a b c a b c", 3),
        ("!@#$%^&*()", 10),
        ("123123456", 6),
    ],
)
def test_length_of_longest_substring(input_string: str, expected_length: int) -> None:
    """
    Test the length_of_longest_substring function with various inputs.

    Args:
        input_string (str): The input string to test.
        expected_length (int): The expected length of the longest substring without repeating characters.

    """
    assert length_of_longest_substring(input_string) == expected_length
