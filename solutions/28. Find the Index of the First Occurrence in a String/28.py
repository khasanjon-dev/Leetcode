def str_str(haystack: str, needle: str) -> int:
    len_needle = len(needle)
    len_haystack = len(haystack)
    for i in range(len_haystack - len_needle + 1):
        if needle == haystack[i: i + len_needle]:
            return i
    return -1


print(str_str("hello", "ll"))

print(str_str("sadbutsad", "sad"))
