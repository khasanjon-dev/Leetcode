def is_path_crossing(path: str) -> bool:
    x, y = 0, 0
    visited = {(0, 0)}
    for move in path:
        if move == 'N':
            y += 1
        elif move == 'S':
            y -= 1
        elif move == 'E':
            x += 1
        elif move == 'W':
            x -= 1
        if (x, y) in visited:
            return True
        visited.add((x, y))
    return False


path = "NESWW"
result = is_path_crossing(path)
print(result)
