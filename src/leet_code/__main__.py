from leet_code.add_two_numbers import ListNode, add_two_numbers
from leet_code.two_sum import two_sum


def two_sum_example() -> None:
    """Example usage of the two_sum function"""
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print("Problem 1: Two Sum")
    print(f"  Indices of the two numbers from {nums} that add up to {target}: {result}")


def add_two_numbers_example() -> None:
    """Example usage of the add_two_numbers function"""
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = add_two_numbers(l1, l2)
    print("Problem 2: Add Two Numbers")
    print(f"  Linked list sum: {l1} + {l2} = {result}")


def main() -> None:
    """Main function to execute the script."""
    two_sum_example()
    add_two_numbers_example()


if __name__ == "__main__":  # pragma: no cover
    main()
