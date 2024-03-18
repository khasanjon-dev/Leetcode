from itertools import chain


def odd_cells(m: int, n: int, indices: list[list[int]]) -> int:
    matrix = [[0] * n for _ in range(m)]
    for index in indices:
        for i, row in enumerate(matrix):
            r = index[0]
            c = index[1]
            for k in range(len(row)):
                if c == k:
                    row[k] += 1
                if r == i:
                    row[k] += 1
    return sum([1 if num % 2 else 0 for num in chain(*matrix)])


print(odd_cells(2, 3, [[0, 1], [1, 1]]))
