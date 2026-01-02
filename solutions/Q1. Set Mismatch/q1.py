def find_error_nums(nums: list[int]) -> list[int]:
    missing = 0
    duplicate = None
    for i in range(len(nums)):
        if i + 1 not in nums:
            missing = i + 1
        if nums[i] in nums[i + 1:]:
            duplicate = nums[i]
    return [duplicate, missing]



print(find_error_nums([1, 2, 2, 4]))