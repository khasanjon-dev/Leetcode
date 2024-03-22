def height_checker(heights: list[int]) -> int:
    result = 0
    heights_sort = sorted(heights)
    for i in range(len(heights)):
        if heights[i] != heights_sort[i]:
            result += 1
    return result


print(height_checker([1, 1, 4, 2, 1, 3]))
