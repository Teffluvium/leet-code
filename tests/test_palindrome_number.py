import pytest

from leet_code.palindrome_number import is_palindrome


@pytest.mark.parametrize(
    "x",
    [
        121,
        12321,
        0,
    ],
)
def test_is_palindrome_true(x: int) -> None:
    """Test the is_palindrome function for palindromic numbers."""
    assert is_palindrome(x) is True


@pytest.mark.parametrize(
    "x",
    [
        -121,
        10,
    ],
)
def test_is_palindrome_false(x: int) -> None:
    """Test the is_palindrome function for non-palindromic numbers."""
    assert is_palindrome(x) is False


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
def test_is_palindrome_no_expected(x: int) -> None:
    """Test the is_palindrome function without expected values."""
    assert is_palindrome(x) is not None
