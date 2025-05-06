def print_visits(visited: list[bool], s: str, j: int) -> None:
    """
    Print the visit status of characters in the string.

    :param visited: List indicating whether a character has been visited
    :param s: Input string
    :param j: Current index in the string
    """
    print(f"s[{j}] = {s[j]}, ", end="")
    print(f"int(s[{j}]) = {ord(s[j])}, ", end="")
    print(f"visited[{ord(s[j])}] = {visited[ord(s[j])]}")


def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.

    :param s: Input string
    :return: Length of the longest substring without repeating characters
    """
    n = len(s)
    max_count = 0
    display_flag = True

    # Assign a bool for all possible characters (initialized to false)
    visited = [False] * 256  # Assuming ASCII characters

    if display_flag:
        print(f"substring: '{s}'")
        print()

    for i in range(n):
        for j in range(i, n):
            if display_flag:
                print_visits(visited, s, j)

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

        if display_flag:
            print(f"current max_count = {max_count}")
            print()

    return max_count


if __name__ == "__main__":
    # Example usage
    input_string = "abcabcbb"
    result = length_of_longest_substring(input_string)
    print(f"Length of the longest substring without repeating characters in '{input_string}': {result}")
    print()
