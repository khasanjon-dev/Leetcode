def minimum_operations(nums: list[int]) -> int:
    operations = sum(0 if num % 3 == 0 else 1 for num in nums)
    return operations


print(minimum_operations([3, 6, 9]))
