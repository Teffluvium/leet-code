from typing import Optional

from leet_code.ListNode import ListNode


def add_two_numbers(
    l1: Optional[ListNode],
    l2: Optional[ListNode],
) -> Optional[ListNode]:
    """
    Add two numbers represented by linked lists.

    :param l1: First number as a linked list
    :param l2: Second number as a linked list
    :return: Sum of the two numbers as a linked list
    """
    # Initialize the result list and carry
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    # Iterate through both lists until both are empty and no carry is left
    while l1 or l2 or carry:
        # Get the values from the lists, defaulting to 0 if empty
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate the sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        # Move to the next nodes in the lists
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next


if __name__ == "__main__":  # pragma: no cover
    # Example usage
    # list_1 = ListNode(2, ListNode(4, ListNode(3)))
    # list_2 = ListNode(5, ListNode(6, ListNode(4)))
    list_1 = ListNode(0)
    list_2 = ListNode(1)
    list_sum = add_two_numbers(list_1, list_2)
    print(f"l1     = {list_1}")
    print(f"l2     = {list_2}")
    print(f"result = {list_sum!s}")

    print()
    # Example usage of from_list method
    list_3 = ListNode.from_iter([2, 4, 3])
    list_4 = ListNode.from_iter([5, 6, 4])
    list_sum_2 = add_two_numbers(list_3, list_4)
    print(f"l1     = {list_3}")
    print(f"l2     = {list_4}")
    print(f"result = {list_sum_2!s}")

    print()
    # Example usage of from_int method
    list_5 = ListNode.from_int(342)
    print(f"list_5 = {list_5}")
