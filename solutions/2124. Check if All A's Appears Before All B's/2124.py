def check_string(s: str) -> bool:
    if len(set(s)) == 1:
        return True
    for i in range(len(s)):
        if s[i] != 'a':
            if set(s[i]) == set(s[i:]):
                return True
            return False


print(check_string('aaabbb'))
