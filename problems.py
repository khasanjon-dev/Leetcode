def fun(words: list[str], left: int, right: int) -> int:
    vowels = 'aeiou'
    result = 0
    for word in words[left: right + 1]:
        if word[0] in vowels and word[-1] in vowels:
            result += 1
    return result


print(fun(['hey', 'aeo', 'mu', 'ooo', 'artro'], 1, 4))
