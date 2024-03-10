def count_pairs(nums: list[int], k: int) -> int:
    count = 0
    nums_len = len(nums)
    if len(set(nums)) == nums_len:
        return 0
    for i in range(nums_len):
        num = nums[i]
        for j in range(i + 1, nums_len):
            if num == nums[j] and i * j % k == 0:
                count += 1
    return count


print(count_pairs([1, 2, 3, 4], 1))
