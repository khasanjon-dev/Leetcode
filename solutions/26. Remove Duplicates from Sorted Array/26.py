def remove_duplicates(nums: list[int]) -> int:
    left = 0
    for right in range(1, len(nums)):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]
    return left + 1


print(remove_duplicates([1, 1]))
