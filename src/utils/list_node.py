# Definition for singly-linked list.
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """
    Definition for singly-linked list.

    Each node contains a single digit and a reference to the next node.
    The digits are stored in reverse order, meaning that the 1's digit is at the head of the list.

    Example:
    The number 123 is represented as 3 -> 2 -> 1.

    Attributes:
        val (int): The value of the node (a single digit).
        next (Optional[ListNode]): A reference to the next node in the list.

    """

    val: int
    next: Optional["ListNode"] = None

    def __str__(self) -> str:
        tmp: ListNode | None = self
        result = []
        while tmp:
            result.append(str(tmp.val))
            tmp = tmp.next
        return f"[{', '.join(result)}]"

    @classmethod
    def from_iter(cls, iterable: "Iterable[int]") -> "ListNode":
        """
        Create a ListNode from an ordered iterable of integers.

        Args:
            iterable (Iterable[int]): An ordered iterable of integers (0-9).

        Returns:
            ListNode: The head of the linked list.

        Raises:
            TypeError: If the input is not an iterable or if it is unordered.
            ValueError: If the iterable is empty or contains invalid integers.

        """
        if not isinstance(iterable, Iterable):
            msg = "Input must be an iterable"
            raise TypeError(msg)

        lst = list(iterable)
        if not lst:
            msg = "Empty iterable"
            raise ValueError(msg)

        try:
            # Try indexing into the iterable to check if it is ordered.
            # This will fail for unordered iterables.
            _ = iterable[0]  # type: ignore[index]
        except TypeError as e:
            msg = "Input must be an ordered iterable"
            raise TypeError(msg) from e

        # Validate that the iterable contains only integers between 0 and 9
        x_min = 0
        x_max = 9
        if not all(isinstance(x, int) and x_min <= x <= x_max for x in lst):
            msg = "Iterable must contain integers between 0 and 9"
            raise ValueError(msg)

        head = cls(lst[0])
        current = head
        for value in lst[1:]:
            current.next = cls(value)
            current = current.next
        return head

    @classmethod
    def from_int(cls, number: int) -> "ListNode":
        """
        Create a ListNode from an integer.

        Args:
            number (int): The integer to convert.

        Returns:
            ListNode: The head of the linked list representing the integer.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the input is a negative integer.

        """
        if not isinstance(number, int):
            msg = "Input must be an integer"
            raise TypeError(msg)

        if number < 0:
            msg = "Number must be non-negative"
            raise ValueError(msg)

        digits = []
        # Extract digits in reverse order
        while number > 0:
            digits.append(number % 10)
            number //= 10

        # Create the linked list from the digits
        head = cls(digits[0])
        current = head
        for digit in digits[1:]:
            current.next = cls(digit)
            current = current.next

        # Return the head of the linked list
        return head
