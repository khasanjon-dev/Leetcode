def row_and_maximum_ones(mat: list[list[int]]) -> list[int]:
    result = [[0, 0]]
    max_ = 0
    for i, row in enumerate(mat):
        count = row.count(1)
        if count > max_:
            max_ = count
            result.append([i, max_])
    return result[-1]


print(row_and_maximum_ones([[0, 0], [0, 0]]))
