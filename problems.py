def fun(text: str, brokenLetters: str) -> int:
    result = 0
    word_list = text.split()
    for word in word_list:
        for letter in brokenLetters:
            if letter in word:
                break
        else:
            result += 1

    return result


print(fun('leet code', 'e'))
