def delete_greatest_value(grid: list[list[int]]) -> int:
    n = len(grid[0])
    result = 0
    for i in range(n):
        max_ = 0
        for row in grid:
            i = row.index(max(row))
            max_ = max(max_, row.pop(i))
        result += max_
    return result


print(delete_greatest_value([[1, 2, 4], [3, 3, 1]]))
