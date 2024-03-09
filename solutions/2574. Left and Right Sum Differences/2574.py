def left_right_difference(nums: list[int]) -> list[int]:
    result = []
    len_nums = len(nums)
    if len_nums > 1:
        for i in range(len_nums):
            result.append(abs(sum(nums[:i]) - sum(nums[i + 1:])))
        return result
    return [0]


print(left_right_difference([1]))
