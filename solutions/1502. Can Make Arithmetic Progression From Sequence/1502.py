def can_make_arithmetic_progression(arr: list[int]) -> bool:
    arr.sort()
    diff = abs(arr[0] - arr[1])
    for i in range(1, len(arr) - 1):
        if diff != abs(arr[i] - arr[i + 1]):
            return False
    return True


print(can_make_arithmetic_progression([1, 2, 4]))
