def detect_capital_use(word: str) -> bool:
    if word.isupper():
        return True
    elif word == word.capitalize():
        return True
    elif word.islower():
        return True
    return False


print(detect_capital_use('FlaG'))
