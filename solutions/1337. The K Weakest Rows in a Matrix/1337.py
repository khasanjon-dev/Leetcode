def k_weakest_rows(mat: list[list[int]], k: int) -> list[int]:
    index_count = {}
    for index, row in enumerate(mat):
        index_count[index] = row.count(1)
    index_count_sorted = sorted(index_count.items(), key=lambda row: row[-1])
    return [row[0] for row in index_count_sorted[:k]]


print(k_weakest_rows(
    [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ],
    3)
)
