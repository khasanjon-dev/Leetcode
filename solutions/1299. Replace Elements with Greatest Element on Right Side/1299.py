def replace_elements(arr: list[int]) -> list[int]:
    if not arr:
        return []

    n = len(arr)
    max_right = -1
    new_arr = [0] * n

    for i in range(n - 1, -1, -1):
        new_arr[i] = max_right
        max_right = max(max_right, arr[i])

    return new_arr


print(replace_elements([17, 18, 5, 4, 6, 1]))
