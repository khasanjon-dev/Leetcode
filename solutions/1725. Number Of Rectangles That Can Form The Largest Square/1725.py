def count_good_rectangles(rectangles: list[list[int]]) -> int:
    count = 0
    min_length = min(max(rectangles))
    for row in rectangles:
        if min(row) == min_length:
            count += 1
    return count


print(count_good_rectangles([[5, 8], [3, 9], [5, 12], [16, 5]]))
