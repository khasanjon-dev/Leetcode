def is_circular_sentence(sentence: str) -> bool:
    sentence_list = sentence.split(" ")
    for i in range(len(sentence_list) - 1):
        if sentence_list[i][-1] != sentence_list[i + 1][0]:
            return False
    return sentence_list[0][0] == sentence_list[-1][-1]


print(is_circular_sentence("leetcode exercises sound delightful"))
