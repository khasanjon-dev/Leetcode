def reverse_words(s: str) -> str:
    def reverse_word(word: str) -> str:
        chars = list(word)
        left, right = 0, len(word) - 1
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        return ''.join(chars)

    reversed_words = []
    for word in s.split():
        reversed_words.append(reverse_word(word))
    return ' '.join(reversed_words)


print(reverse_words("hello world"))
