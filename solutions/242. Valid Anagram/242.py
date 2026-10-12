def is_anagram(s: str, t: str) -> bool:
    def count_chars(s: str) -> dict:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        return counts
    return count_chars(s) == count_chars(t)


print(is_anagram(s="anagram", t="nagaram"))
