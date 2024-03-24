def find_duplicate(nums: list[int]) -> int:
    i = 0
    while i <= len(nums):
        if nums.count(nums[i]) >= 2:
            return nums[i]
        i += 1


print(find_duplicate([1, 3, 4, 2, 2]))
