def next_greatest_letter(letters: list[str], target: str) -> str:
    for letter in letters:
        if letter > target:
            return letter
    return letters[0]


print(next_greatest_letter(letters=["x", "x", "y", "y"], target="z"))
