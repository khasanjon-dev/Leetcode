def count_vowel_substring(word: str) -> int:
    vowels = set("aeiou")
    n = len(word)
    ans = 0

    for i in range(n):
        seen = set()
        for j in range(i, n):
            if word[j] not in vowels:
                break
            seen.add(word[j])
            if len(seen) == 5:
                ans += 1

    return ans


print(count_vowel_substring("aeiouu"))
