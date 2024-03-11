def count_good_rectangles(rectangles: list[list[int]]) -> int:
    sa = max(sorted(rectangles))
    print(sa)


print(count_good_rectangles([[5, 8], [3, 9], [5, 12], [16, 5]]))
