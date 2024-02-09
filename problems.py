def largest_divisible_subset(nums):
    if not nums:
        return []
    n = len(nums)
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [nums[i]]

    return max(dp, key=len)


nums = [1, 2, 3, 4, 6]
print(largest_divisible_subset(nums))
