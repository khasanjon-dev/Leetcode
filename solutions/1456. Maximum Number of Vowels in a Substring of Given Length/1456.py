def max_vowels(s: str, k: int) -> int:
    def count_vowels(word: str) -> int:
        vowels = 0

        for char in word:

            if char in 'aeiou':
                vowels += 1

        return vowels

    max_vowels = 0

    for i in range(0, len(s) - k + 1):
        max_vowels = max(max_vowels, count_vowels(s[i: i + k]))

    return max_vowels


print(max_vowels(s="abciiidef", k=3))
