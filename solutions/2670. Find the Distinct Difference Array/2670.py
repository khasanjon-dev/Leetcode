def distinct_difference_array(nums: list[int]) -> list[int]:
    return [len(set(nums[:i + 1])) - len(set(nums[i + 1:])) for i in range(len(nums))]


print(distinct_difference_array([3, 2, 3, 4, 2]))
