def num_different_integers(word: str) -> int:
    result = []
    res = ''
    for w in word:
        if w.isdigit():
            res += w
        else:
            if res:
                result.append(int(res))
            res = ''
    if res:
        result.append(int(res))
    return len(set(result))


print(num_different_integers('a1b01c001'))
