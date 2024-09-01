def find_max_k(nums: list[int]) -> int:
    nums = set(nums)
    return max((num for num in nums if -num in nums), default=-1)


print(find_max_k([-1, 2, -3, 3]))
