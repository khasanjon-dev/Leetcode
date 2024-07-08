def find_words(words: list[str]) -> list[str]:
    first_row = 'qwertyuiop'
    second_row = 'asdfghjkl'
    third_row = 'zxcvbnm'
    result = []

    for word in words:
        word_lower = word.lower()
        if word_lower[0] in first_row:
            for w in word_lower:
                if w not in first_row:
                    break
            else:
                result.append(word)
        elif word_lower[0] in second_row:
            for w in word_lower:
                if w not in second_row:
                    break
            else:
                result.append(word)
        elif word_lower[0] in third_row:
            for w in word_lower:
                if w not in third_row:
                    break
            else:
                result.append(word)
    return result


print(find_words(['Hello', 'Alaska', 'Dad', 'Peace']))
