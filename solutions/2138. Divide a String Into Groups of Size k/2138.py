def divide_string(s: str, k: int, fill: str) -> list[str]:
    result = []
    for i in range(0, len(s), k):
        result.append(s[i: i + k])
    len_last = len(result[-1])
    if len_last != k:
        result.append(result.pop() + fill * (k - len_last))
    return result


print(divide_string('abcdefghij', 3, 'x'))
