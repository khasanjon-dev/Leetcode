def reverse_str(s: str, k: int) -> str:
    res = ''
    for i in range(0, len(s), 2 * k):
        res += s[i:i + k][::-1] + s[i + k: i + 2 * k]
    return res


print(reverse_str('abcd', 2))
