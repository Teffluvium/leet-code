def int_to_roman(num: int) -> str:
    """Convert an integer to a Roman numeral.

    Roman numerals are represented by seven different symbols:

    | Symbol | Value |
    | -----: | :---- |
    |   `I`  |     1 |
    |   `V`  |     5 |
    |   `X`  |    10 |
    |   `L`  |    50 |
    |   `C`  |   100 |
    |   `D`  |   500 |
    |   `M`  |  1000 |

    Note:
        This function assumes that the input integer is within the range of 1 to 3999,
        as Roman numerals are not typically used for numbers outside this range.

    Args:
        num (int): The integer to convert.

    Returns:
        str: The Roman numeral representation of the integer.

    Raises:
        ValueError: If the input integer is not between 1 and 3999.
    """
    if num <= 0 or num >= 4000:
        raise ValueError("Input must be between 1 and 3999.")

    rom_symbols = [
        "M",
        "CM",
        "D",
        "CD",
        "C",
        "XC",
        "L",
        "XL",
        "X",
        "IX",
        "V",
        "IV",
        "I",
    ]
    rom_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result_roman_numeral = ""

    for symbol, value in zip(rom_symbols, rom_values):
        while num >= value:
            result_roman_numeral += symbol
            num -= value

    return result_roman_numeral


def roman_to_int(s: str) -> int:
    """Convert a Roman numeral to an integer.

    Args:
        s (str): The Roman numeral to convert.

    Returns:
        int: The integer representation of the Roman numeral.
    """
    if s == "MMMM":
        raise ValueError("Invalid Roman numeral: 'MMMM' is not allowed.")
    if not s:
        raise ValueError("Invalid Roman numeral: empty string is not allowed.")

    rom: dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    result_integer = 0

    # Loop over the string in reverse order
    prev_value = 0

    for char in reversed(s):
        # Check if the character is in the dictionary
        value = rom.get(char, 0)
        if value < prev_value:
            # If the value is less than the previous value, subtract it
            result_integer -= value
        else:
            # Otherwise, add it to the result
            result_integer += value

        # Update the previous value
        prev_value = value

    return result_integer


if __name__ == "__main__":  # pragma: no cover
    # Example usage
    number = 1994
    roman_numeral = int_to_roman(number)
    print(f"The Roman numeral for {number} is: {roman_numeral}")

    # Example usage of roman_to_int
    roman_string = "MCMXCIV"
    integer_value = roman_to_int(roman_string)
    print(f"The integer value of the Roman numeral '{roman_string}' is: {integer_value}")
