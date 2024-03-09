def sum_counts(nums: list[int]) -> int:
    result = 0
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(len_nums - i):
            result += len(set(nums[j: j + i + 1])) ** 2
    return result


print(sum_counts([1, 1]))
