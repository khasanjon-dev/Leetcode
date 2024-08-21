def final_position_of_snake(n: int, commands: list[str]) -> int:
    grids = [list(num for num in range(i, i + n)) for i in range(0, n * n, n)]
    row, column = 0, 0
    for command in commands:
        if command == "RIGHT":
            row += 1
        elif command == "LEFT":
            row -= 1
        elif command == "UP":
            column -= 1
        elif command == "DOWN":
            column += 1
    return grids[column][row]


print(final_position_of_snake(2, ["RIGHT", "DOWN"]))
