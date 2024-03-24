def maximum_strong_pair_xor(nums: list[int]) -> int:
    max_ = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            a = nums[i]
            b = nums[j]
            if abs(a - b) <= min(a, b):
                max_ = max(max_, a ^ b)
    return max_


print(maximum_strong_pair_xor([10, 100]))
