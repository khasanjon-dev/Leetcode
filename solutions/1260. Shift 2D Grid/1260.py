from itertools import chain


def shift_grid(grid: list[list[int]], k: int) -> list[list[int]]:
    m, n = len(grid), len(grid[0])
    total = m * n
    flat = list(chain(*grid))
    k %= total
    flat = flat[-k:] + flat[:-k]

    return [flat[i * n:(i + 1) * n] for i in range(m)]


print(shift_grid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
