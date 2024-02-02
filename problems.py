def number_game(nums: list[int]) -> list[int]:
    result = []
    for _ in range(len(nums) // 2):
        min_1, min_2 = nums.pop(nums.index(min(nums))), nums.pop(nums.index(min(nums)))
        result.extend([min_2, min_1])
    return result


print(number_game([2, 5]))
