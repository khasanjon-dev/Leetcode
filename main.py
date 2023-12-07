from collections import Counter


def fun(s: str) -> bool:
    counter = Counter(s)
    num = counter[s[0]]
    for value in counter.values():
        if not num == value:
            return False
    return True


print(fun("abacbc"))
