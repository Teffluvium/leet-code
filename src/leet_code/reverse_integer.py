def reverse_integer(x: int) -> int:
    """Reverse the digits of an integer.
    :param x: The integer to reverse
    :return: The reversed integer, or 0 if the result is outside the 32-bit signed integer range.
    """
    sign = -1 if x < 0 else 1

    x = abs(x)
    reversed_x = 0
    while x != 0:
        digit = x % 10  # Get the least significant digit
        x //= 10  # Remove the least significant digit from x

        # Construct the reversed integer
        reversed_x = reversed_x * 10 + digit

        # Check for overflow
        if reversed_x > 2**31 - 1:
            return 0

    return sign * reversed_x


if __name__ == "__main__":
    # Example usage
    print(f"{reverse_integer(123) = }")  # Output: 321
    print(f"{reverse_integer(-123) = }")  # Output: -321
    print(f"{reverse_integer(120) = }")  # Output: 21
    print(f"{reverse_integer(1002) = }")  # Output: 2001
    print(f"{reverse_integer(0) = }")  # Output: 0
    print(f"{reverse_integer(1534236469) = }")  # Output: 0 (overflow case)
