def max_repeating(sequence: str, word: str) -> int:
    repeats = 0
    words = word
    while words in sequence:
        repeats += 1
        words += word
    return repeats


print(max_repeating('aaabaaaabaaabaaaabaaaabaaaabaaaaba', 'aaaba'))
