def maximum_number_of_string_pairs(words: list[str]) -> int:
    result = 0
    for i, word in enumerate(words):
        if words[i + 1:].count(word[::-1]):
            result += 1
    return result


print(maximum_number_of_string_pairs(["cd", "ac", "dc", "ca", "zz"]))
