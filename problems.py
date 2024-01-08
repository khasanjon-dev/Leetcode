def make_smallest_palindrome(s: str) -> str:
    result = ''
    l = len(s)
    a = s[: l // 2]
    c = None
    if l % 2:
        b = s[l // 2 + 1:]
        c = s[l // 2]
    else:
        b = s[l // 2:]
    res = ''
    for i in range(1, len(a) + 1):
        if a[i - 1] != b[-i]:
            if a[i - 1] > b[-i]:
                res += b[-i]
            else:
                res += a[i - 1]
        else:
            res += a[i - 1]
    if c:
        result += res + c + res[::-1]
    else:
        result += res + res[::-1]
    return result


print(make_smallest_palindrome('egcfe'))
