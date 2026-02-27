def min_operations(s: str, k: int) -> int:
    n = len(s)
    flips = [0] * n
    res = 0
    flip_count = 0

    for i in range(n):
        if i >= k:
            flip_count -= flips[i - k]

        if (int(s[i]) + flip_count) % 2 == 0:
            if i + k > n:
                return -1
            flips[i] = 1
            flip_count += 1
            res += 1

    return res


print(min_operations("110", 1))
