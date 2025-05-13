from contextlib import nullcontext as does_not_raise

import pytest

from leet_code.ListNode import ListNode


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
            # Unordered iterable case
            {1, 2, 3},
            None,
            pytest.raises(IndexError),
            "Input must be an ordered iterable",
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
        assert str(expected) == str(result)
