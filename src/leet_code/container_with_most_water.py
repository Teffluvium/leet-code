def max_area(height: list[int]) -> int:
    """
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
    n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
    Find two lines, which together with the x-axis forms a container, such that the container contains the most water.

    Notice that you may not slant the container.

    Args:
        height (list[int]): List of non-negative integers representing the heights of the lines.

    Returns:
        int: The maximum area of water that can be contained by the lines.
    """
    largest_area = 0
    ind_start = 0
    ind_end = len(height) - 1
    current_height = 0
    current_area = 0

    while ind_start < ind_end:
        current_height = min(height[ind_start], height[ind_end])
        current_area = current_height * (ind_end - ind_start)

        # Update the maximum area if current area is greater
        if current_area > largest_area:
            largest_area = current_area

        # Move the shorter line towards the center
        if height[ind_start] < height[ind_end]:
            ind_start += 1
        else:
            ind_end -= 1

    # Return the maximum area found
    return largest_area


if __name__ == "__main__":  # pragma: no cover
    # Example usage
    height_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = max_area(height_list)
    print(f"Maximum area of the container: {result}")
