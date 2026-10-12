def first_unique_char(s: str) -> int:
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for i, char in enumerate(s):
        if counts[char] == 1:
            return i
    return -1


print(first_unique_char("leetcode"))
