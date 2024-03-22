def smallest_equal(nums: list[int]) -> int:
    for i, num in enumerate(nums):
        if i % 10 == num:
            return i
    return -1


print(smallest_equal([7, 8, 3, 5, 2, 6, 3, 1, 1, 4, 5, 4, 8, 7, 2, 0, 9, 9, 0, 5, 7, 1, 6]))
