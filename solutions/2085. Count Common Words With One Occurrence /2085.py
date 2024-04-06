def count_words(words1: list[str], words2: list[str]) -> int:
    result = 0
    for word in words2:
        if word in words1 and words1.count(word) == 1 == words2.count(word):
            result += 1
    return result


print(count_words(["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"]))
