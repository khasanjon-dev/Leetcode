def min_removal(nums: list[int], k: int) -> int:
    nums.sort()
    n = len(nums)
    max_keep, l = 1, 0
    for m in range(n):
        while nums[m] > nums[l] * k:
            l += 1
        max_keep = max(max_keep, m - l + 1)
    return n - max_keep


print(min_removal([2, 1, 5], 2))
