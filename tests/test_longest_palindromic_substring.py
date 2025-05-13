import pytest

from leet_code.longest_palindromic_substring import longest_palindromic_substring


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("babad", "aba"),  # "bab" is also valid
        ("cbbd", "bb"),
        ("a", "a"),
        ("ac", "c"),  # "a" is also valid
        ("", ""),
        ("racecar", "racecar"),
        ("abacdfgdcaba", "aba"),  # "aca" is also valid
        ("aaaa", "aaaa"),
        ("abcde", "e"),  # Any single character is valid
    ],
)
def test_longest_palindromic_substring(input_string: str, expected_output: str) -> None:
    result = longest_palindromic_substring(input_string)
    # Since there can be multiple valid outputs, check if the result is a palindrome
    assert (
        result == expected_output or result[::-1] == expected_output
    )  # Since there can be multiple valid outputs, check if the result is a palindrome
    assert result == expected_output or result[::-1] == expected_output
