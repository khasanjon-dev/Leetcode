from collections import Counter


def find_shortest_subarray(nums: list[int]) -> int:
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    return max(counts, key=counts.get)


print(find_shortest_subarray([1, 2, 2, 3, 1]))
