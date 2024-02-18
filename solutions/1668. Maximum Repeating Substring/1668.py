def max_repeating(sequence: str, word: str) -> int:
    result = 0
    words = word
    while words in sequence:
        result += 1
        words += word
    return result


print(max_repeating('aaabaaaabaaabaaaabaaaabaaaabaaaaba', 'aaaba'))
