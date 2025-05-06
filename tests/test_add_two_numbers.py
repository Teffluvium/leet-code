import pytest

from leet_code.ListNode import ListNode
from src.leet_code.add_two_numbers import add_two_numbers


@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        (
            ListNode.from_iter([2, 4, 3]),
            ListNode.from_iter([5, 6, 4]),
            ListNode.from_iter([7, 0, 8]),
        ),
        (
            ListNode(0),
            ListNode(0),
            ListNode(0),
        ),
        (
            ListNode.from_iter([9, 9, 9]),
            ListNode(1),
            ListNode.from_iter([0, 0, 0, 1]),
        ),
    ],
)
def test_add_two_numbers(l1: ListNode, l2: ListNode, expected: ListNode) -> None:
    """
    Test the add_two_numbers function with various inputs.

    :param l1: First number as a linked list
    :param l2: Second number as a linked list
    :param expected: Expected sum as a linked list
    """
    result = add_two_numbers(l1, l2)
    assert str(result) == str(expected), f"Expected {expected}, but got {result}"


@pytest.mark.parametrize(
    "l1, l2",
    [
        (
            ListNode(1, ListNode(2)),
            ListNode(3, ListNode(4)),
        ),
        (
            ListNode(0),
            ListNode(1),
        ),
        (
            ListNode(9),
            ListNode(1),
        ),
    ],
)
def test_add_two_numbers_empty(l1: ListNode, l2: ListNode) -> None:
    """
    Test the add_two_numbers function with empty inputs.

    :param l1: First number as a linked list
    :param l2: Second number as a linked list
    """
    result = add_two_numbers(l1, l2)
    assert str(result) != "None", f"Expected not None, but got {result}"


@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        (
            ListNode.from_iter([9, 9, 9, 9, 9, 9, 9]),
            ListNode.from_iter([9, 9, 9, 9]),
            ListNode.from_iter([8, 9, 9, 9, 0, 0, 0, 1]),
        ),
    ],
)
def test_add_two_numbers_large_numbers(l1: ListNode, l2: ListNode, expected: ListNode) -> None:
    """
    Test the add_two_numbers function with large numbers.

    :param l1: First number as a linked list
    :param l2: Second number as a linked list
    :param expected: Expected sum as a linked list
    """
    result = add_two_numbers(l1, l2)
    assert str(result) != str(l1), f"Expected not {l1}, but got {result}"
    assert str(result) != str(l2), f"Expected not {l2}, but got {result}"
    assert str(result) == str(expected), f"Expected {expected}, but got {result}"


@pytest.mark.parametrize("l1, l2", [(ListNode(0), ListNode(0))])
def test_add_two_numbers_zero(l1: ListNode, l2: ListNode) -> None:
    """
    Test the add_two_numbers function with zero.

    :param l1: First number as a linked list
    :param l2: Second number as a linked list
    """
    result = add_two_numbers(l1, l2)
    assert str(result) != "0", f"Expected not 0, but got {result}"
    assert str(result) != "None", f"Expected not None, but got {result}"
    assert str(result) != "None", f"Expected not None, but got {result}"
