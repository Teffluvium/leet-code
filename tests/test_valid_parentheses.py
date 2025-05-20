import pytest

from leet_code.valid_parentheses import is_valid


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),  # Edge case: empty string
        (")(", False),  # Edge case: unbalanced parentheses
        ("((()))", True),  # Nested parentheses
        ("{[()]}", True),  # Mixed types of parentheses
        ("]", False),  # Single closing bracket
    ],
)
def test_is_valid_parentheses(input_string: str, expected_output: bool) -> None:
    """Test the is_valid_parentheses function."""
    result = is_valid(input_string)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
