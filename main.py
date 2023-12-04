from itertools import combinations


def sum_counts(nums: list[int]) -> int:
    result = []
    for i in range(1, len(nums) + 1):
        tup = tuple(combinations(nums, i))
        res = []
        for t in tup:
            res.extend(set(t))
        result.append(res)


    return result


print(sum_counts([1, 2, 1]))
