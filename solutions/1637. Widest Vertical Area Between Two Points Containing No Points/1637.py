def max_width_of_vertical_area(points: list[list[int]]) -> int:
    def sort_x(point):
        x, y = point[0], point[1]
        return x

    points_sort = sorted(points, key=sort_x)
    max_vertical = 0
    for i in range(len(points_sort) - 1):
        difference = points_sort[i + 1][0] - points_sort[i][0]
        if difference > max_vertical:
            max_vertical = difference
    return max_vertical


print(max_width_of_vertical_area([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))
