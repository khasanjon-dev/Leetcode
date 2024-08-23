def greatest_letter(s: str) -> str:
    max_letter = 0
    for letter in s:
        ascii_letter = ord(letter)
        if letter.isupper() and chr(ascii_letter + 32) in s:
            max_letter = max(ascii_letter, max_letter)

    return chr(max_letter) if max_letter else ''


print(greatest_letter("AbCdEfGhIjK"))
