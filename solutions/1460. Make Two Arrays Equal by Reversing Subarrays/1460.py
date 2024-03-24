def can_be_equal(target: list[int], arr: list[int]) -> bool:
    return sorted(target) == sorted(arr)


print(can_be_equal([809, 107, 274], [809, 274, 107]))
