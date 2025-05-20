import pytest

from leet_code.valid_parentheses import is_valid


@pytest.mark.parametrize(
    "input_string",
    [
        "()",
        "()[]{}",
        "{[]}",
        "",  # Edge case: empty string
        "((()))",  # Nested parentheses
        "{[()]}",  # Mixed types of parentheses
    ],
)
def test_is_valid_parenthesis_true(input_string: str) -> None:
    """Test the True reposonses of is_valid_parentheses function."""
    result: bool = is_valid(input_string)
    assert result is True, f"Expected {True}, but got {result}"


@pytest.mark.parametrize(
    "input_string",
    [
        "(]",
        "([)]",
        ")(",  # Edge case: unbalanced parentheses
        "]",  # Single closing bracket
    ],
)
def test_is_valid_parenthesis_false(input_string: str) -> None:
    """Test the False reposonses of is_valid_parentheses function."""
    result: bool = is_valid(input_string)
    assert result is False, f"Expected {False}, but got {result}"
