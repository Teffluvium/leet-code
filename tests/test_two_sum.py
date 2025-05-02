# create tests for two_sum.py
import pytest

from src.leet_code.two_sum import two_sum


@pytest.mark.parametrize(
    "num_list, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3], 5, [1, 2]),
        ([0, -1, 2], 1, [1, 2]),
    ],
)
def test_two_sum(num_list: list[int], target: int, expected: list[int]) -> None:
    """
    Test the two_sum function with various inputs.

    :param num_list: List of integers
    :param target: Target integer
    :param expected: Expected output list of indices
    """
    result = two_sum(num_list, target)
    assert result == expected, f"Expected {expected}, but got {result}"


@pytest.mark.parametrize(
    "num_list, target",
    [
        ([1, 2, 3], 10),
        ([0, 0, 0], 1),
        ([], 0),
        ([1], 1),
        ([1, 2], 4),
    ],
)
def test_two_sum_no_solution(num_list: list[int], target: int) -> None:
    """
    Test the two_sum function with inputs that have no solution.

    :param num_list: List of integers
    :param target: Target integer
    """
    result = two_sum(num_list, target)
    assert result == [], f"Expected [], but got {result}"
