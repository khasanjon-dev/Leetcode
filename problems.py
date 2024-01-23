def string_matching(words: list[str]) -> list[str]:
    result = []
    for i, w in enumerate(words):
        for j, word in enumerate(words):
            if w in word and i != j:
                result.append(w)
                break
    return result


print(string_matching(['leetcoder', 'leetcode', 'od', 'hamlet', 'am']))
