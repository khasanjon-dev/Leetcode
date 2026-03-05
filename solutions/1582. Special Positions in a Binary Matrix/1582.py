def num_special(mat: list[list[int]]) -> int:
    result = 0
    m = len(mat)
    n = len(mat[0])
    columns_sum = {}
    for p in range(n):
        column_sum = 0
        for q in range(m):
            column_sum += mat[q][p]
        columns_sum[p] = column_sum

    for i in range(m):
        row_sum = sum(mat[i])
        for j in range(n):
            if mat[i][j] == 1:
                if row_sum == 1 and columns_sum[j] == 1:
                    result += 1
    return result


print(num_special([[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
