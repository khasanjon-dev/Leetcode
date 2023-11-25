s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]


def restore_string(s: str, indices: list[int]) -> str:
    result = ''
    res = {}
    for i, v in enumerate(indices):
        res[v] = s[i]
    res = sorted(res.items())
    for _, value in res:
        result += value
    return result


print(restore_string(s, indices))
