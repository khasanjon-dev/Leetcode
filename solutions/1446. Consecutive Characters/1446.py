def max_power(s: str) -> int:
    res = [1]
    count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            res.append(count)
            count = 1
    res.append(count)
    return max(res)


print(max_power('cc'))
