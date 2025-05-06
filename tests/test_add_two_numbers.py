from contextlib import nullcontext as does_not_raise

import pytest

from src.leet_code.add_two_numbers import ListNode, add_two_numbers


@pytest.mark.parametrize(
    "py_iter, expected, exception, message",
    [
        (
            # Good case
            [1, 2, 3],
            ListNode(1, ListNode(2, ListNode(3))),
            does_not_raise(),
            None,
        ),
        (
            # Non-iterable case
            123,
            None,
            pytest.raises(TypeError),
            "Input must be an iterable",
        ),
        (
            # Empty iterable case
            [],
            None,
            pytest.raises(ValueError),
            "Empty iterable",
        ),
        (
            # Negative integer case
            [-1, 2, 3],
            None,
            pytest.raises(ValueError),
            "Iterable must contain integers between 0 and 9",
        ),
    ],
)
def test_list_node_from_iter_with_exceptions(
    py_iter: list,
    expected: ListNode,
    exception: type,
    message: str,
) -> None:
    """
    Test the from_iter method of ListNode with exceptions.

    :param py_iter: Python iterable (e.g., list, tuple, ) used to create ListNode
    :param expected: Expected ListNode
    :param exception: Exception type to be raised
    :param message: Message to be displayed if the test fails
    """
    with exception as exc_info:
        result = ListNode.from_iter(py_iter)
    assert message is None or str(exc_info.value) == message

    # Check the result only if no exception is raised
    if expected is not None:
        assert str(expected) == str(result)


@pytest.mark.parametrize(
    "py_iter, expected, exception, message",
    [
        (
            # Good case
            1_007,
            ListNode(7, ListNode(0, ListNode(0, ListNode(1)))),
            does_not_raise(),
            None,
        ),
        (
            # Non-integer case
            123.6,
            None,
            pytest.raises(TypeError),
            "Input must be an integer",
        ),
        (
            # Negative integer case
            -123,
            None,
            pytest.raises(ValueError),
            "Number must be non-negative",
        ),
    ],
)
def test_list_node_from_int_with_exceptions(
    py_iter: list,
    expected: ListNode,
    exception: type,
    message: str,
) -> None:
    """
    Test the from_iter method of ListNode with exceptions.

    :param py_iter: Python iterable (e.g., list, tuple, ) used to create ListNode
    :param expected: Expected ListNode
    :param exception: Exception type to be raised
    :param message: Message to be displayed if the test fails
    """
    with exception as exc_info:
        result = ListNode.from_int(py_iter)
    assert message is None or str(exc_info.value) == message

    # Check the result only if no exception is raised
    if expected is not None:
        assert str(expected) == str(result)


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
