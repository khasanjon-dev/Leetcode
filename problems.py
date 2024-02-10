def count_substring(s: str) -> int:
    count = 0
    l = len(s)
    for i in range(l):
        for j in range(i + 1, l + 1):
            word = s[i: j]
            if word == word[::-1]:
                count += 1

    return count


print(count_substring('aaaaa'))
