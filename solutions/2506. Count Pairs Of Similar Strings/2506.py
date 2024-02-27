# def similar_pairs(words: list[str]) -> int:
#     count = 0
#     for i, word in enumerate(words):
#         word = tuple(sorted(set(word)))
#         for j in range(i + 1, len(words)):
#             w = tuple(sorted(set(words[j])))
#             if w == word:
#                 count += 1
#     return count
#
#
# print(similar_pairs(["aba", "aabb", "abcd", "bac", "aabc"]))

def similar_pairs(words: list[str]) -> int:
    count = 0
    len_words = len(words)
    for i in range(len_words):
        word_1 = ''
        for w in words[i]:
            if w not in word_1:
                word_1 += w
        word_1 = ''.join(sorted(word_1))
        for j in range(i + 1, len_words):
            word_2 = ''
            for w in words[j]:
                if w not in word_2:
                    word_2 += w
            word_2 = ''.join(sorted(word_2))
            if word_1 == word_2:
                count += 1

    return count


print(similar_pairs(["aba", "aabb", "abcd", "bac", "aabc"]))
