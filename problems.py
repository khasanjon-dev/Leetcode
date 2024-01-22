def detect_capital_use(word: str) -> bool:
    res = 0
    for w in word:
        if 65 <= ord(w) <= 90:
            res += 1
    if res == len(word):
        return True
    elif res == 1:
        for w in word[1:]:
            if 65 <= ord(w) <= 90:
                return False
        return True
    elif res == 0:
        return True
    return False


print(detect_capital_use('FlaG'))
