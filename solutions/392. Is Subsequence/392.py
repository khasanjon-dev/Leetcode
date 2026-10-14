def is_subsequence(s: str, t: str) -> bool:
    s_index = 0

    for char in t:

        if s_index < len(s) and s[s_index] == char:
            s_index += 1

    return s_index == len(s)


print(is_subsequence(s="abc", t="ahbgdc"))
