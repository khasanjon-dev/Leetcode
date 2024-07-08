def digit_sum(s: str, k: int) -> str:
    while len(s) > k:
        w = ''
        for i in range(0, len(s), k):
            w += str(sum([int(n) for n in s[i: i + k]]))
        s = w
    return s


print(digit_sum('1234', 2))
