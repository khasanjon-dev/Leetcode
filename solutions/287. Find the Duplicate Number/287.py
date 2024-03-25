from collections import Counter


def find_duplicate(nums: list[int]) -> int:
    counter_nums = sorted(Counter(nums).items(), key=lambda item: -item[-1])
    return counter_nums[0][0]


print(find_duplicate([1, 3, 4, 2, 2]))
