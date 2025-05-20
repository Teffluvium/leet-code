import pytest

from leet_code.longest_common_prefix import longest_common_prefix


@pytest.mark.parametrize(
    "input_strs, expected_output",
    [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["a", "a", "a"], "a"),
        (["", "", ""], ""),
        (["abc", "abc", "abc"], "abc"),
        ([], ""),  # Edge case: empty list
        (["single"], "single"),  # Edge case: single string
    ],
)
def test_longest_common_prefix(input_strs: list[str], expected_output: str) -> None:
    """Test the longest_common_prefix function."""
    result = longest_common_prefix(input_strs)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
