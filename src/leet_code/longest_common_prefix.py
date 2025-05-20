def longest_common_prefix(strs: list[str]) -> str:
    """
    Find the longest common prefix string among an array of strings.

    Args:
        strs (list[str]): List of strings to find the common prefix.

    Returns:
        str: The longest common prefix. If there is no common prefix, return an empty string.
    """
    if not strs:
        return ""

    # Start with the first string as the prefix
    s1 = strs[0]
    prefix = ""

    for s in s1:
        # Loop through remaining strings
        for word in strs[1:]:
            # If the current character does not match, return the prefix
            if not word.startswith(prefix + s):
                return prefix

        # If all strings match, add the character to the prefix
        prefix += s

    # If we reach here, all characters matched
    return prefix


if __name__ == "__main__":  # pragma: no cover
    # Example usage
    input_strings = ["flower", "flow", "flight"]
    # input_strings = ["dog", "racecar", "car"]
    result = longest_common_prefix(input_strings)
    print(f"The longest common prefix is: '{result}'")
