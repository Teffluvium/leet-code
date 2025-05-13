def my_atoi(s: str) -> int:
    """
    Convert a string to an integer (similar to C's atoi function).

    The function discards all leading whitespace characters and reads the
    following characters until the first non-digit character or the end of
    the string is reached. The function also handles optional leading '+' or
    '-' signs to indicate the sign of the number. If no valid conversion can
    be performed, the function returns 0. The function also handles overflow
    and underflow conditions, returning the maximum or minimum integer value
    as appropriate.

    The function assumes that the input string is a valid representation of
    an integer, and it does not handle any other characters or formats.
    The function is case-sensitive and only recognizes the characters '0' to
    '9' as valid digits.

    Example:
        Input: "   -42"
        Output: -42

    Args:
        s (str): The input string to convert.

    Returns:
        int: The converted integer.
    """
    int_min = -(2**31)
    int_max = 2**31 - 1

    # Remove leading whitespace
    s = s.lstrip()
    if not s:
        return 0

    # Check for sign characters
    sign = -1 if s[0] == "-" else 1

    # Skip sign character
    if s[0] in ["-", "+"]:
        s = s[1:]

    my_int: int = 0

    for char in s:
        if not char.isdigit():
            break

        # Construct the integer from each digit
        digit = int(char)
        my_int = my_int * 10 + digit

        # Return early if result exceeds the limits
        if sign == 1 and my_int > int_max:
            return int_max
        if sign == -1 and my_int > -int_min:
            return int_min

    return sign * my_int


if __name__ == "__main__":  # pragma: no cover
    # Example usage
    input_str = "   -42"
    result = my_atoi(input_str)
    print(f"Converted integer from '{input_str}': {result}")
