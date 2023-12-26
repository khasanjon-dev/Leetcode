def find_non_min_or_max(nums: list[int]) -> int:
    nums = list(set(nums))
    if len(nums) <= 2:
        return -1
    nums.sort()
    return nums[1]


print(find_non_min_or_max([3, 2, 1, 4]))
