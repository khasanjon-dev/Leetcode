def remove_element(nums: list[int], val: int) -> int:
    left = 0
    for right in range(len(nums)):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
    return left

print(remove_element(nums=[3, 2, 2, 3], val=3))
