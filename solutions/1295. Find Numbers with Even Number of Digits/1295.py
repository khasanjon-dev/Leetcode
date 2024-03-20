def find_numbers(nums: list[int]) -> int:
    return sum([1 for num in nums if len(str(num)) % 2 == 0])



print(find_numbers([12, 345, 2, 6, 7896]))
