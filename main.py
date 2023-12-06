def is_acronym(words: list[str], s: str) -> bool:
    res = ''
    for word in words:
        res += word[0]
    return res == s


print(is_acronym(['alice', 'bob', 'charlie'], 'abc'))
