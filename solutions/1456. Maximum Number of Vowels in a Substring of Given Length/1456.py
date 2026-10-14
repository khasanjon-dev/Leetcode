def max_vowels(s: str, k: int) -> int:
    vowels = set("aeiou")

    window_count = sum(char in vowels for char in s[:k])
    max_count = window_count

    for i in range(k, len(s)):
        window_count += s[i] in vowels
        window_count -= s[i - k] in vowels

        max_count = max(max_count, window_count)

        if max_count == k:
            return k

    return max_count


print(max_vowels(s="abciiidef", k=3))
