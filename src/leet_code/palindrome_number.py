def is_palindrome(x: int) -> bool:
    """Check if an integer is a palindrome.
    A palindrome is a number that remains the same when its digits are reversed.

    Args:
        x (int): The integer to check.

    Returns:
        bool: True if x is a palindrome, False otherwise.
    """

    reverse = 0
    copy = x

    while copy > 0:
        digit = copy % 10
        copy //= 10

        reverse = reverse * 10 + digit

    return reverse == x


if __name__ == "__main__":  # pragma: no cover
    print(f"{is_palindrome(121) = }")  # True
    print(f"{is_palindrome(-121) = }")  # False
    print(f"{is_palindrome(10) = }")  # False
    print(f"{is_palindrome(12321) = }")  # True
    print(f"{is_palindrome(0) = }")  # True
