import pytest

from leet_code.reverse_integer import reverse_integer


@pytest.mark.parametrize(
    "x, expected",
    [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (1534236469, 0),  # Overflow case
        (-1534236469, 0),  # Overflow case
    ],
)
def test_reverse_integer(x: int, expected: int) -> None:
    """
    Test the reverse_integer function with various inputs.

    :param x: Input integer
    :param expected: Expected output integer after reversal
    """
    result = reverse_integer(x)
    assert result == expected, f"Expected {expected}, but got {result}"
