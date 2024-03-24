from collections import Counter


def frequency_sort(nums: list[int]) -> list[int]:
    nums.sort(reverse=True)
    counter = Counter(nums)
    sorted_nums = sorted(nums, key=lambda num: (counter[num], nums.index(num)))
    return sorted_nums


print(frequency_sort([2, 3, 1, 3, 2]))
# [1, 3, 3, 2, 2]
