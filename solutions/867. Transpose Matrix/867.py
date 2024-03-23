def transpose(matrix: list[list[int]]) -> list[list[int]]:
    zip_matrix = list(zip(*matrix))
    new_matrix = []
    for mat in zip_matrix:
        new_matrix.append(list(mat))
    return new_matrix

print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
