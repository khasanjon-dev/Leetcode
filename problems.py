def count_pairs(nums: list[int], target: int) -> int:
    result = 0
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(i + 1, len_nums):
            if nums[i] + nums[j] < target:
                result += 1
    return result


print(count_pairs([-6, 2, 5, -2, -7, -1, 3], -2))
