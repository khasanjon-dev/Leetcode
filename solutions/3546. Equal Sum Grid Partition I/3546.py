def can_partition_grid(grid: list[list[int]]) -> bool:
    m, n = len(grid), len(grid[0])

    total_sum = sum(sum(row) for row in grid)
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2

    top_sum = 0
    for i in range(m - 1):
        top_sum += sum(grid[i])
        if top_sum == target:
            return True

    col_sums = [0] * n
    for j in range(n):
        for i in range(m):
            col_sums[j] += grid[i][j]

    left_sum = 0
    for j in range(n - 1):
        left_sum += col_sums[j]
        if left_sum == target:
            return True

    return False


print(can_partition_grid([[1, 3, 3], [2, 3, 2]]))


"""
[
    [1, 3, 3],
    [2, 3, 2]
]
"""
