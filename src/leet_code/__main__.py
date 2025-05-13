from leet_code import palindrome_number, string_to_integer, zigzag_conversion
from leet_code.add_two_numbers import add_two_numbers
from leet_code.length_of_longest_substring import length_of_longest_substring
from leet_code.ListNode import ListNode
from leet_code.longest_palindromic_substring import longest_palindromic_substring
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


def longest_substring_example() -> None:
    """Example usage of the length_of_longest_substring function"""
    input_string = "abcabcbb"
    result = length_of_longest_substring(input_string)
    print("Problem 3: Longest Substring Without Repeating Characters")
    print(f"  Length of the longest substring without repeating characters in '{input_string}': {result}")


def longest_palindromic_substring_example() -> None:
    """Example usage of the longest_palindromic_substring function"""
    input_string = "babad"
    result = longest_palindromic_substring(input_string)
    print("Problem 5: Longest Palindromic Substring")
    print(f"  Longest palindromic substring in '{input_string}': {result}")


def ziggzag_conversion_example() -> None:
    """Example usage of the zigzag_conversion function"""
    s = "PAYPALISHIRING"
    num_rows = 3
    result = zigzag_conversion.convert(s, num_rows)
    print("Problem 6: Zigzag Conversion")
    print(f"  Zigzag conversion of '{s}' with {num_rows} rows: {result}")


def string_to_integer_example() -> None:
    """Example usage of the string_to_integer function"""
    input_string = "   -42"
    result = string_to_integer.my_atoi(input_string)
    print("Problem 8: String to Integer (atoi)")
    print(f"  Converted integer from '{input_string}': {result}")


def palindrome_number_example() -> None:
    """Example usage of the is_palindrome function"""
    input_number = 121
    result = palindrome_number.is_palindrome(input_number)
    print("Problem 9: Palindrome Number")
    print(f"  Is {input_number} a palindrome? {result}")


def main() -> None:
    """Main function to execute the script."""
    two_sum_example()
    add_two_numbers_example()
    longest_substring_example()
    longest_palindromic_substring_example()
    ziggzag_conversion_example()
    string_to_integer_example()
    palindrome_number_example()


if __name__ == "__main__":  # pragma: no cover
    main()
