def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.

    Args:
        s (str): Input string

    Returns:
        int: Length of the longest substring without repeating characters
    """
    n = len(s)
    max_count = 0

    # Assign a bool for all possible characters (initialized to false)
    visited = [False] * 256  # Assuming ASCII characters

    for i in range(n):
        for j in range(i, n):
            # Check if this character has been seen before in this substring
            if visited[ord(s[j])]:
                break

            else:
                # Otherwise, update the visited status and the max_count
                max_count = max(max_count, j - i + 1)
                visited[ord(s[j])] = True

        # Shift the sliding window and reset the status for the first character
        # of the previous window
        visited[ord(s[i])] = False

    return max_count


if __name__ == "__main__":  # pragma: no cover
    # Example usage
    input_string = "abcabcbb"
    result = length_of_longest_substring(input_string)
    print(f"Length of the longest substring without repeating characters in '{input_string}': {result}")
    print()
