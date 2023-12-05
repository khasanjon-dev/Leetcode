from itertools import combinations, chain


def sum_counts(nums: list[int]) -> int:
    res = []
    for i in range(2, len(nums) + 1):
        l = list(combinations(nums, i))
        r = []
        for t in l:
            if len(set(t)) == 1:
                pass
            else:
                r.extend(t)
        res.append(r)
    res.append(nums)
    result = sum([num ** 2 for num in chain(*res)])

    print(result)


print(sum_counts([1, 2, 1]))
