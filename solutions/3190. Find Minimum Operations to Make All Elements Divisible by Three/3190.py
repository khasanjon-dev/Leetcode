def minimum_operations(nums: list[int]) -> int:
    operations = sum(1 for num in nums if num % 3)
    return operations


print(minimum_operations([3, 6, 9]))
