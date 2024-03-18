def remove_palindrome_sub(s: str) -> int:
    step_count = 0
    if s == s[::-1]:
        return step_count + 1
    while s:
        pass

    for i in range(len(s)):
        if s[i + 1:] == s[i + 1:][::-1]:
            step_count += 1


print(remove_palindrome_sub('abb'))
