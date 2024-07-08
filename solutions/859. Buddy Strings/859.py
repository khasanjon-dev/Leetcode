def buddy_strings(s: str, goal: str) -> bool:
    first_index = False
    if len(s) != len(goal):
        return False
    if s == goal and len(s) > 2 and len(s) > len(set(s)) or len(set(s)) == 1 and len(s) > 1:
        return True
    for i in range(len(s)):
        if s[i] != goal[i]:
            if isinstance(first_index, bool):
                first_index = i
            else:
                print(s[:first_index] + s[i] + s[first_index + 1: i] + s[first_index] + s[i + 1:])
                if s[:first_index] + s[i] + s[first_index + 1: i] + s[first_index] + s[i + 1:] == goal:
                    return True
                return False
    return False


print(buddy_strings("aa", "a"))
