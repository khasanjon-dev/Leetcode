def construct_rectangle(area: int) -> list[int]:
    width = int(area ** (1 / 2))
    while area % width != 0:
        width -= 1
    length = area // width
    return [length, width]


print(construct_rectangle(20))
