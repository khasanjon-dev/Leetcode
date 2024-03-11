def separate_digits(nums: list[int]) -> list[int]:
    separate_nums = []
    for num in nums:
        separate_nums.extend([int(n) for n in str(num)])
    return separate_nums


print(separate_digits([13, 25, 83, 77]))
