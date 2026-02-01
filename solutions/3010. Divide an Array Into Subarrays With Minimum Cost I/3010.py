def minimum_cost(nums: list[int]) -> int:
    first = nums[0]
    second = float("inf")
    third = float("inf")
    for num in nums[1:]:
        if num < second:
            third = second
            second = num
        elif num < third:
            third = num
    return first + second + third


print(minimum_cost([5, 4, 3]))
