def count_valid_words(sentence: str) -> int:
    def is_valid(word: str) -> bool:
        count_hy = 0
        for i, c in enumerate(word):
            if c.isdigit():
                return False
            if c == '-':
                if i == 0 or not word[i - 1].isalpha():
                    return False
                if i == len(word) - 1 or not word[i + 1].isalpha():
                    return False
                if count_hy == 1:
                    return False
                count_hy += 1
            if c in ['!', '.', ',']:
                if i != len(word) - 1:
                    return False
        return True

    return sum(is_valid(word) for word in sentence.split())
