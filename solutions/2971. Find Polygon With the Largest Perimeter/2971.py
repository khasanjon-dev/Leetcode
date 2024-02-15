def largest_perimeter(nums: list[int]) -> int:
    prefix = sum(nums)
    for num in sorted(nums, reverse=True):
        prefix -= num
        if prefix > num:
            return prefix + num
    return -1


print(largest_perimeter([1, 12, 1, 2, 5, 50, 3]))
