def two_sum(num_list: list[int], target: int) -> list[int]:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    Args:
        num_list (list[int]): List of integers.
        target (int): Target integer.

    Returns:
        list[int]: List of indices of the two numbers.

    """
    # Initialize a dictionary to store the indices of the numbers
    num_dict: dict[int, int] = {}

    for index, num in enumerate(num_list):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], index]
        num_dict[num] = index

    return []


if __name__ == "__main__":  # pragma: no cover
    # Example usage
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")
