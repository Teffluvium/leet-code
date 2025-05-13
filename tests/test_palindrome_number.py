import pytest

from leet_code.palindrome_number import is_palindrome


@pytest.mark.parametrize(
    "x, expected",
    [
        (121, True),
        (-121, False),
        (10, False),
        (12321, True),
        (0, True),
    ],
)
def test_is_palindrome(x, expected):
    """Test the is_palindrome function."""
    assert is_palindrome(x) == expected


@pytest.mark.parametrize(
    "x",
    [
        (121),
        (-121),
        (10),
        (12321),
        (0),
    ],
)
def test_is_palindrome_no_expected(x):
    """Test the is_palindrome function without expected values."""
    assert is_palindrome(x) is not None
