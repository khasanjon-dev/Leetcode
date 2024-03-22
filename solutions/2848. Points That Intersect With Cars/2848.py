from itertools import chain


def number_of_points(nums: list[list[int]]) -> int:
    nums_range = []
    for row in nums:
        nums_range.append([num for num in range(row[0], row[1] + 1)])
    nums_set = set(chain(*nums_range))
    return len(nums_set)


print(number_of_points([[1, 3], [5, 8]]))
