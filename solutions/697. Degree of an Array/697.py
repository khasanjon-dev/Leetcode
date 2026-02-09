def find_shortest_subarray(nums: list[int]) -> int:
    counter = {}
    first, last = {}, {}
    for i, num in enumerate(nums):
        counter[num] = counter.get(num, 0) + 1
        if num not in first:
            first[num] = i
        last[num] = i

    degree = max(counter.values())
    res = len(nums)
    for num in counter:
        if counter[num] == degree:
            res = min(res, last[num] - first[num] + 1)
    return res


print(find_shortest_subarray([1, 2, 2, 3, 1]))
