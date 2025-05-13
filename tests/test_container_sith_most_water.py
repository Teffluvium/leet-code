import pytest

from leet_code.container_with_most_water import max_area


@pytest.mark.parametrize(
    "height, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([2, 3, 10, 5, 7, 8, 9], 36),
        ([0], 0),
        ([1], 0),
        ([1, 2], 1),
    ],
)
def test_max_area(height: list[int], expected: int) -> None:
    """
    Test the max_area function with various inputs.

    Args:
        height (list[int]): List of non-negative integers representing the heights of the lines.
        expected (int): Expected maximum area of water that can be contained by the lines.
    """
    assert max_area(height) == expected
