from itertools import chain


def count_negatives(grid: list[list[int]]) -> int:
    return len(list(filter(lambda x: True if x < 0 else False, list(chain(*grid)))))


print(count_negatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
