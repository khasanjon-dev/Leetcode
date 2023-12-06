def final_string(s: str) -> str:
    res = ''
    for w in s:
        if w == 'i':
            res = res[::-1]
        else:
            res += w
    return res


print(final_string('string'))