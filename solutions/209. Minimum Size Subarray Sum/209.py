def min_sub_array_len(target: int, nums: list[int]) -> int:
    window_sum = 0
    left = 0
    nums_len = len(nums)

    for i in range(nums_len):
        temp = 0

        while window_sum < target:
            window_sum += nums[temp]
        else:


        temp += 1


print(min_sub_array_len(target=7, nums=[2, 3, 1, 2, 4, 3]))
