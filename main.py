def fun(word: str, ch: str):
    i = 0
    for w in word:
        i += 1
        if w == ch:
            break
    if i:
        result = ''
        result += word[:i][::-1]
        return result + word[i:]
    return word


print(fun('abcdefd', 'd'))
