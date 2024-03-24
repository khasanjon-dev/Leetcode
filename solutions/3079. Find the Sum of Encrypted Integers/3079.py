def sum_of_encrypted_int(nums: list[int]) -> int:
    return sum([int(max(str(num)) * len(str(num))) for num in nums])


print(sum_of_encrypted_int([10, 21, 31]))
