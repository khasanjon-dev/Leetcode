def split_word_by_seperator(words: list[str], separator: str) -> list[str]:
    result = []
    for word in words:
        if separator in word:
            res = ''
            for w in word:
                if w == separator:
                    if res:
                        result.append(res)
                        res = ''
                else:
                    res += w
            if res:
                result.append(res)
        else:
            result.append(word)
    return result


print(split_word_by_seperator(["$easy$", "$problem$"], "$"))
