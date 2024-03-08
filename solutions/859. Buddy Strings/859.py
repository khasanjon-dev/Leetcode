def buddy_strings(s: str, goal: str) -> bool:
    # if len(set(s + goal)) == 1:
    #     return True
    # if len(s) != len(goal) or s == goal and len(s) == 2:
    #     return False
    # count = 0
    # char_s = ''
    # char_g = ''
    # for i in range(len(s)):
    #     if s[i] != goal[i]:
    #         char_s += s[i]
    #         char_g += goal[i]
    #         count += 1
    #         if count == 3:
    #             return False
    # if char_g == char_s[::-1]:
    #     return True
    # return False
    if len(set(s + goal)) == 1:
        return True
    if len(s) != len(goal) or s == goal and len(s) == 2:
        return False
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == goal[j] and s[j] == goal[i] and s[:i] == goal[:j] and s[j + 1:] == goal[i + 1:]:
                return True
    return False


print(buddy_strings("abcd", "badc"))
