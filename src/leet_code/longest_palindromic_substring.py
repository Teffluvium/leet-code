def expand_around_center(s: str, left: int, right: int) -> int:
    """
    Expand around the center to find the length of the longest palindromic
    substring.

    Args:
        s (str): Input string
        left (int): Left index
        right (int): Right index

    Returns:
        int: Length of the palindromic substring
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1


def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring in a given string.

    Args:
        s (str): Input string

    Returns:
        str: Longest palindromic substring
    """
    if not s:
        return ""

    # Initialize indices for the position of the longest palindrome
    start = 0
    end = 0

    for i in range(len(s)):
        odd_pal_len = expand_around_center(s, i, i)  # Odd length palindrome
        even_pal_len = expand_around_center(s, i, i + 1)  # Even length palindrome
        max_len = max(odd_pal_len, even_pal_len)

        if max_len > (end - start):
            # The palindrome is centered at index i.
            # Start and end indices are relative to the center.
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    # Slice the string to get the longest palindromic substring
    return s[start : (end + 1)]


if __name__ == "__main__":  # pragma: no cover
    # Example usage
    input_string = "babad"
    result = longest_palindromic_substring(input_string)
    print(f"Longest palindromic substring in '{input_string}': {result}")
    print()
