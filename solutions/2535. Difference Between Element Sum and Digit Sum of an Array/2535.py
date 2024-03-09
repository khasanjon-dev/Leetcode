def difference_of_sum(nums: list[int]) -> int:
    num_sum = 0
    for num in nums:
        num = str(num)
        if len(num) > 1:
            for n in num:
                num_sum += int(n)
        else:
            num_sum += int(num)
    return abs(sum(nums)) - num_sum


print(difference_of_sum([1, 15, 6, 3]))
