def min_sub_sequence(nums: list[int]) -> list[int]:
    nums.sort(reverse=True)
    for i in range(1, len(nums) + 1):
        if sum(nums[:i]) > sum(nums[i:]):
            return nums[:i]


print(min_sub_sequence([4, 4, 7, 6, 7]))
