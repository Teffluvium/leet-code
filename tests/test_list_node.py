from contextlib import nullcontext as does_not_raise

import pytest

from leet_code.list_node import ListNode


@pytest.mark.parametrize(
    ("py_iter", "expected", "exception"),
    [
        (
            # Good case
            1_007,
            ListNode(7, ListNode(0, ListNode(0, ListNode(1)))),
            does_not_raise(),
        ),
        (
            # Non-integer case
            123.6,
            None,
            pytest.raises(TypeError, match="Input must be an integer"),
        ),
        (
            # Negative integer case
            -123,
            None,
            pytest.raises(ValueError, match="Number must be non-negative"),
        ),
    ],
)
def test_list_node_from_int_with_exceptions(
    py_iter: int,
    expected: ListNode,
    exception: pytest.ExceptionInfo[Exception],
) -> None:
    """
    Test the from_int method of ListNode with exceptions.

    Args:
        py_iter (int): The integer to convert to a ListNode.
        expected (ListNode): The expected ListNode representation.
        exception (pytest.ExceptionInfo[Exception]): The expected exception context.

    """
    with exception:  # type: ignore[attr-defined]
        result = ListNode.from_int(py_iter)
        if expected is not None:
            assert str(expected) == str(result)


@pytest.mark.parametrize(
    ("py_iter", "expected", "exception"),
    [
        (
            # Good case
            [1, 2, 3],
            ListNode(1, ListNode(2, ListNode(3))),
            does_not_raise(),
        ),
        (
            # Non-iterable case
            123,
            None,
            pytest.raises(TypeError, match="Input must be an iterable"),
        ),
        (
            # Unordered iterable case
            {1, 2, 3},
            None,
            pytest.raises(TypeError, match="Input must be an ordered iterable"),
        ),
        (
            # Empty iterable case
            [],
            None,
            pytest.raises(ValueError, match="Empty iterable"),
        ),
        (
            # Negative integer case
            [-1, 2, 3],
            None,
            pytest.raises(ValueError, match="Iterable must contain integers between 0 and 9"),
        ),
    ],
)
def test_list_node_from_iter_with_exceptions(
    py_iter: list,
    expected: ListNode,
    exception: pytest.ExceptionInfo[Exception],
) -> None:
    """
    Test the from_iter method of ListNode with exceptions.

    Args:
        py_iter (list): _description_
        expected (ListNode): _description_
        exception (pytest.ExceptionInfo[Exception]): _description_

    """
    with exception:  # type: ignore[attr-defined]
        result = ListNode.from_iter(py_iter)
        if expected is not None:
            assert str(expected) == str(result)
