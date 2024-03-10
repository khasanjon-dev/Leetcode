def sum_of_squares(nums: list[int]) -> int:
    sum_squares = 0
    nums_len = len(nums)
    for i, num in enumerate(nums, 1):
        if nums_len % i == 0:
            sum_squares += num ** 2
    return sum_squares


print(sum_of_squares([2, 7, 1, 19, 18, 3]))
