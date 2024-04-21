def make_fancy_string(s: str) -> str:
    result = ''
    count = 0
    word = s[0]
    for i in range(1, len(s)):
        if s[i] == word:
            count += 1
        else:
            if count >= 2:
                count = 0
                result += word * 2
                word = s[i]
            else:
                result += word
                word = s[i]
                count = 0
    # result += s[i]
    return result


print(make_fancy_string('aaabaaaa'))
