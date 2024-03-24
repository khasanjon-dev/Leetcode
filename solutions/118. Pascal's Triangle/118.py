def generate(numRows: int) -> list[list[int]]:
    result = [[1]]
    for i in range(1, numRows):
        res = [1]
        for j in range(i):
            res.append(sum(result[i - 1][j: j + 2]))
        result.append(res)
    return result


print(generate(5))
