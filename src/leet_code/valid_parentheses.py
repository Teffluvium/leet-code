"""Check if a string containing parentheses is valid."""


def is_valid(s: str) -> bool:
    """
    Check if the input string s contains valid parentheses.

    Args:
        s (str): The input string containing parentheses.

    Returns:
        bool: True if the parentheses are valid, False otherwise.

    """
    stack: list[str] = []
    mapping: dict[str, str] = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    for char in s:
        # Check if char is a closing parenthesis
        if char in mapping:
            # Check if char is a closing parenthesis and matches the last opened one
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                # If stack is empty or doesn't match, return False
                return False
        else:
            stack.append(char)

    # Stack should be empty if all parentheses are valid
    return not stack


if __name__ == "__main__":  # pragma: no cover
    # Example usage
    input_string: str = "{[()]}"
    result: bool = is_valid(input_string)
    print(f"The parentheses in '{input_string}' are valid: {result}")
