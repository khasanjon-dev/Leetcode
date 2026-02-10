def longest_balanced(nums: list[int]) -> int:
    res = 0
    nums_len = len(nums)
    for i in range(nums_len):
        even, odds = set(), set()
        for j in range(i, nums_len):
            if nums[j] % 2 == 0:
                even.add(nums[j])
            else:
                odds.add(nums[j])

            if len(even) == len(odds):
                res = max(res, j - i + 1)
    return res


print(longest_balanced([1, 2, 3, 2]))
