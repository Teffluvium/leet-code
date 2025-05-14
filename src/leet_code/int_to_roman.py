from collections import OrderedDict


def int_to_roman(num: int) -> str:
    """Convert an integer to a Roman numeral.

    Roman numerals are represented by seven different symbols:

    | Symbol  | Value |
    | ------: | :-----|
    |   `I`     |     1 |
    |   `V`     |     5 |
    |   `X`     |    10 |
    |   `L`     |    50 |
    |   `C`     |   100 |
    |   `D`     |   500 |
    |   `M`     |  1000 |

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

    rom: OrderedDict[str, int] = OrderedDict([
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    ])
    result_roman_numeral = ""

    for symbol, value in rom.items():
        while num >= value:
            result_roman_numeral += symbol
            num -= value

    return result_roman_numeral


if __name__ == "__main__":  # pragma: no cover
    # Example usage
    number = 1994
    roman_numeral = int_to_roman(number)
    print(f"The Roman numeral for {number} is: {roman_numeral}")
