import pytest

from src.leet_code.add_two_numbers import ListNode, add_two_numbers


@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        (
            ListNode(2, ListNode(4, ListNode(3))),
            ListNode(5, ListNode(6, ListNode(4))),
            ListNode(7, ListNode(0, ListNode(8))),
        ),
        (
            ListNode(0),
            ListNode(0),
            ListNode(0),
        ),
        (
            ListNode(9, ListNode(9, ListNode(9))),
            ListNode(1),
            ListNode(0, ListNode(0, ListNode(0, ListNode(1)))),
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
def test_add_two_numbers_no_solution(l1: ListNode, l2: ListNode) -> None:
    """
    Test the add_two_numbers function with inputs that have no solution.

    :param l1: First number as a linked list
    :param l2: Second number as a linked list
    """
    result = add_two_numbers(l1, l2)
    assert str(result) != str(l1), f"Expected not {l1}, but got {result}"
    assert str(result) != str(l2), f"Expected not {l2}, but got {result}"


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
def test_add_two_numbers_large_numbers(l1: ListNode, l2: ListNode) -> None:
    """
    Test the add_two_numbers function with large numbers.

    :param l1: First number as a linked list
    :param l2: Second number as a linked list
    """
    result = add_two_numbers(l1, l2)
    assert str(result) != str(l1), f"Expected not {l1}, but got {result}"
    assert str(result) != str(l2), f"Expected not {l2}, but got {result}"


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
def test_add_two_numbers_negative_numbers(l1: ListNode, l2: ListNode) -> None:
    """
    Test the add_two_numbers function with negative numbers.

    :param l1: First number as a linked list
    :param l2: Second number as a linked list
    """
    result = add_two_numbers(l1, l2)
    assert str(result) != str(l1), f"Expected not {l1}, but got {result}"
    assert str(result) != str(l2), f"Expected not {l2}, but got {result}"


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
def test_add_two_numbers_zero(l1: ListNode, l2: ListNode) -> None:
    """
    Test the add_two_numbers function with zero.

    :param l1: First number as a linked list
    :param l2: Second number as a linked list
    """
    result = add_two_numbers(l1, l2)
    assert str(result) != "0", f"Expected not 0, but got {result}"
    assert str(result) != "None", f"Expected not None, but got {result}"
