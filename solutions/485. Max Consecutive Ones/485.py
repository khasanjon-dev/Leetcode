def find_max_consecutive_ones(nums: list[int]) -> int:
    result = counter = 0
    for num in nums:
        if num:
            counter += 1
        else:
            result = max(result, counter)
            counter = 0
    return max(result, counter)


print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))
