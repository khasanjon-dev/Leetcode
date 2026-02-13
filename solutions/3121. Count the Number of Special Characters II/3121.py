def number_of_special_chars(word: str) -> int:
    last_lower = {}
    first_upper = {}

    for i, ch in enumerate(word):
        if ch.islower():
            last_lower[ch] = i
        else:
            lower_char = ch.lower()
            if lower_char not in first_upper:
                first_upper[lower_char] = i

    count = 0

    for c in last_lower:
        if c in first_upper and last_lower[c] < first_upper[c]:
            count += 1

    return count


print(number_of_special_chars("aaAbcBC"))
