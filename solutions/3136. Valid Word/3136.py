def is_valid(word: str) -> bool:
    vowels = 'aeiou'
    if len(word) >= 3:
        is_alpha_or_number, is_vowel, is_consonant = True, False, False
        for w in word:
            if not w.isdigit() and not w.isalpha():
                is_alpha_or_number = False
            elif w.lower() in vowels:
                is_vowel = True
            elif w.isalpha() and w.lower() not in vowels:
                is_consonant = True
        return is_vowel and is_alpha_or_number and is_consonant
    return False


print(is_valid("UuE6"))
