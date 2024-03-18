def unequal_triplets(nums: list[int]) -> int:
    count = 0
    nums_len = len(nums)
    for i in range(0, nums_len - 2):
        for j in range(i + 1, nums_len - 1):
            for k in range(j + 1, nums_len):
                if len(set((nums[i], nums[j], nums[k]))) == 3:
                    count += 1

    return count


print(unequal_triplets([1, 1, 1, 1, 1]))
