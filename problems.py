def arithmetic_triplets(nums: list[int], diff: int) -> int:
    l = len(nums)
    result = 0
    for i in range(l):
        num = nums[i]
        for j in range(i + 1, l):
            if diff == nums[j] - num:
                for k in range(j + 1, l):
                    if diff == nums[k] - nums[j]:
                        result += 1
                        break
    return result


print(arithmetic_triplets([4, 5, 6, 7, 8, 9], 2))
