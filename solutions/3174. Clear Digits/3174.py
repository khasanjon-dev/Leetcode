def clear_digits(s: str) -> str:
    result = []
    for i in range(len(s)):
        if s[i].isdigit():
            result.pop()
        else:
            result.append(s[i])
    return ''.join(result)


print(clear_digits('gbysb5'))
