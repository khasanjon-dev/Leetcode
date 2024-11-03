def rotate_string(s: str, goal: str) -> bool:
    for i in range(len(s)):
        if s[i:] + s[:i] == goal:
            return True
    return False


print(rotate_string("abcde", "cdeab"))
