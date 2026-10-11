def move_zeros(nums: list[int]) -> list[int]:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            if left != right:
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums


print(move_zeros([1]))
