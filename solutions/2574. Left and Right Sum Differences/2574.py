def left_right_difference(nums: list[int]) -> list[int]:
    return [abs(sum(nums[:i]) - sum(nums[i + 1:])) for i in range(len(nums))]


print(left_right_difference([1]))
