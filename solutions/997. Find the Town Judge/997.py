def find_judge(n: int, trust: list[list[int]]) -> int:
    if n == 1:
        return 1

    trust_score = [0] * (n + 1)

    for a, b in trust:
        trust_score[a] -= 1
        trust_score[b] += 1

    for i in range(1, n + 1):
        if trust_score[i] == n - 1:
            return i

    return -1


print(find_judge(3, [[1, 3], [2, 3]]))
