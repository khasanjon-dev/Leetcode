def second_highest(s: str) -> int:
    res = []
    for w in s:
        if w.isnumeric():
            if (num := int(w)) not in res:
                res.append(num)
    if len(res) >= 2:
        return sorted(set(res))[-2]
    return -1


print(second_highest('dfa12321afd'))
