def smaller_numbers_than_current(nums: list[int]) -> list[int]:
    sorted_nums = sorted(nums)

    nums_dict = {}
    for i, n in enumerate(sorted_nums):
        if n not in nums_dict:
            nums_dict[n] = i

    return [nums_dict[n] for n in nums]


print(smaller_numbers_than_current([8, 1, 1, 2, 2, 2, 2, 3]))
