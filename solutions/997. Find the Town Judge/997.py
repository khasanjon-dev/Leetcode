def find_judge(n: int, trust: list[list[int]]) -> int:
    result = {}
    for a, b in trust:
        if a in result:
            result[a].append(b)
        else:
            result[a] = [b]
    values = sorted(result.values())
    if len(result) != n - 1:
        return -1
    elif n == 1 and not trust:
        return 1
    for nums in values:
        for num in nums:
            if all(num in value for value in values):
                return num
    return -1


print(find_judge(1, []))
"""
1-> 3,4
2-> 3,4
4-> 3


1: [3, 4]

"""
