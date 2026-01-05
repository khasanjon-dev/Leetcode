def find_disappeared_numbers(nums: list[int]) -> list[int]:
    len_nums = len(nums)
    set_nums = set(nums)
    result = []
    for num in range(1, len_nums + 1):
        if not num in set_nums:
            result.append(num)
    return result


print(find_disappeared_numbers([1, 1]))
