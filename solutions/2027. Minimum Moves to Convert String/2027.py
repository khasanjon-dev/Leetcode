def minimum_moves(s: str) -> int:
    step = 0
    i = 0
    while i < len(s):
        if s[i] == "O":
            i += 1
            continue
        elif "X" in s[i : i + 3]:
            step += 1
            i += 3
    return step


print(minimum_moves("OXOOX"))
