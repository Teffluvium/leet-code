import pytest

from leet_code.zigzag_conversion import convert


@pytest.mark.parametrize(
    "s, num_rows, expected",
    [
        ("", 1, ""),
        ("A", 0, "A"),
        ("A", 1, "A"),
        ("AB", 1, "AB"),
        ("ABC", 2, "ACB"),
        ("ABCD", 1, "ABCD"),
        ("ABCDE", 0, "ABCDE"),
        ("ABCDE", 3, "AEBDC"),
        ("PAYPALISHIRING", 1, "PAYPALISHIRING"),
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("PAYPALISHIRING", 5, "PHASIYIRPLIGAN"),
    ],
)
def test_zigzag_conversion(s: str, num_rows: int, expected: str) -> None:
    """
    Test the zigzag_conversion function with various inputs.

    :param s: Input string
    :param num_rows: Number of rows for zigzag conversion
    :param expected: Expected output string after zigzag conversion
    """
    result = convert(s, num_rows)
    assert result == expected, f"Expected {expected}, but got {result}"
