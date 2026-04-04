def find_rotation(mat: list[list[int]], target: list[list[int]]) -> bool:
    for _ in range(4):
        if mat == target:
            return True
        mat = [list(row) for row in zip(*mat[::-1])]
    return False
