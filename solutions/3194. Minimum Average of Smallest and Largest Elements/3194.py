def minimum_average(nums: list[int]) -> float:
    averages = []
    for _ in range(len(nums) // 2):
        max_num = max(nums)
        min_num = min(nums)
        averages.append((max_num + min_num) / 2)
        nums.remove(max_num), nums.remove(min_num)

    return min(averages)


print(minimum_average([7, 8, 3, 4, 15, 13, 4, 1]))
