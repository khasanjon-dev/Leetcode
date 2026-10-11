def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        if current_area > max_water:
            max_water = current_area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
