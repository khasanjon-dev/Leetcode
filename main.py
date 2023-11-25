def running_sum(nums: list[int]) -> list[int]:
    # result = []
    # for i in range(len(nums)):
    #     result.append(sum(nums[:i + 1]))
    return [sum(nums[:i + 1]) for i in range(len(nums))]


# Input:
nums = [1, 2, 3, 4]
# Output:
# [1, 3, 6, 10] -> [1, 1+2, 1+2+3, 1+2+3+4]


print(running_sum(nums))
