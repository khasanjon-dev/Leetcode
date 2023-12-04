def num_identical_paris(nums: list[int]) -> int:
    result = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                result += 1
    return result


print(num_identical_paris([1, 2 ,3]))
