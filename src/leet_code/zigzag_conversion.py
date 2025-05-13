def convert(input_str: str, num_rows: int) -> str:
    """
    Convert a string to a zigzag pattern on a given number of rows and
    read it line by line.

    Example:
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given
        number of rows like this: (you may want to display this pattern in a
        fixed font for better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R

        And then read line by line: "PAHNAPLSIIGYIR"

    Args:
        input_str (str): The input string to be converted
        num_rows (int): The number of rows for the zigzag pattern

    Returns:
        str: The zigzag converted string
    """
    if num_rows <= 0:
        return input_str

    if num_rows == 1 or num_rows >= len(input_str):
        return input_str

    result_list: list[str] = [""] * num_rows
    zigzag_idx: int = 0
    forward: bool = True

    for letter in input_str:
        # Append the letter the current row of the zigzag pattern
        result_list[zigzag_idx] += letter

        # Move to the next row index of the zigzag pattern
        if forward:
            zigzag_idx += 1
        else:
            zigzag_idx -= 1

        # Change the direction if we reach the top or bottom row
        if zigzag_idx == num_rows - 1:
            forward = False
        elif zigzag_idx == 0:
            forward = True

    # Join the strings in each row to form the final result
    return "".join(result_list)


if __name__ == "__main__":  # pragma: no cover
    # Example usage
    s = "PAYPALISHIRING"
    numRows = 3
    result = convert(s, numRows)
    expected_result = "PAHNAPLSIIGYIR"
    print(f"Zigzag conversion of '{s}' with {numRows} rows: {result}")
    print(f"Expected result: {expected_result}")
