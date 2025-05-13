# Definition for singly-linked list.
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """Definition for singly-linked list.

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
        tmp: Optional[ListNode] = self
        result = []
        while tmp:
            result.append(str(tmp.val))
            tmp = tmp.next
        return f"[{', '.join(result)}]"

    @classmethod
    def from_iter(cls, iterable: "Iterable[int]") -> "ListNode":
        """Create a ListNode from an ordered iterable of integers."""

        if not isinstance(iterable, Iterable):
            raise TypeError("Input must be an iterable")

        lst = list(iterable)
        if not lst:
            raise ValueError("Empty iterable")

        try:
            # Try indexing into the iterable to check if it's ordered
            _ = iterable[0]
        except IndexError as exc:
            raise IndexError("Input must be an ordered iterable") from exc

        # Validate that the iterable contains only integers between 0 and 9
        if not all(isinstance(x, int) and 0 <= x <= 9 for x in lst):
            raise ValueError("Iterable must contain integers between 0 and 9")

        head = cls(lst[0])
        current = head
        for value in lst[1:]:
            current.next = cls(value)
            current = current.next
        return head

    @classmethod
    def from_int(cls, number: int) -> "ListNode":
        """Create a ListNode from an integer."""
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")

        if number < 0:
            raise ValueError("Number must be non-negative")

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
