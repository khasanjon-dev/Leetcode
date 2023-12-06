from string import ascii_lowercase as lower


def fun(s: str):
    result = []
    for i, w in enumerate(s):
        if w == '#':
            result.pop()
            result.pop()
            result.append(lower[int(s[i - 2: i]) - 1])
        else:
            result.append(lower[int(s[i]) - 1])
    res = ''
    for w in result:
        res += w
    return res


print(fun('10#11#12'))
