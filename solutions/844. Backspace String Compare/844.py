def backspace_compare(s: str, t: str) -> bool:
    def next_valid_char(word: str, index: int) -> int:
        backspaces = 0
        while index >= 0:
            if word[index] == "#":
                backspaces += 1
            elif backspaces > 0:
                backspaces -= 1
            else:
                return index
            index -= 1
        return -1

    i, j = len(s) - 1, len(t) - 1
    while i >= 0 or j >= 0:
        i = next_valid_char(s, i)
        j = next_valid_char(t, j)
        if i == -1 and j == -1:
            return True
        if i == -1 or j == -1:
            return False
        if s[i] != t[j]:
            return False
        i -= 1
        j -= 1
    return True


print(backspace_compare(s="ab#c", t="ad#c"))
