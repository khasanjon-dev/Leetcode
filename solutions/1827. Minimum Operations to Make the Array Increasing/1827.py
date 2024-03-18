def min_operations(nums: list[int]) -> int:
    count = 0
    for i in range(1, len(nums)):
        num1 = nums[i - 1]
        num2 = nums[i]
        if num1 > num2:
            difference = num1 - num2 + 1
            count += difference
            nums[i] += difference
        if num1 == num2:
            count += 1
            nums[i] += 1
    return count


print(min_operations([1, 1, 1]))
