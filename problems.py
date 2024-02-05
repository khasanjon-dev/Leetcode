def first_uniq_char(s: str) -> int:
    for i, w in enumerate(s):
        if s.count(w) == 1:
            return i
    return -1


print(first_uniq_char("loveleetcode"))


def first_uniq_char(s: str) -> int:
    for i in range(len(s)):
        if s[i] not in s[i + 1:] and s[i] not in s[:i]:
            return i
    return -1


print(first_uniq_char("loveleetcode"))
