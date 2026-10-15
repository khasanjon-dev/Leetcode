def min_sub_array_len(target: int, nums: list[int]) -> int:
    left = 0
    window_sum = 0
    len_nums = len(nums)
    min_len = len_nums + 1

    for right in range(len_nums):
        window_sum += nums[right]

        while window_sum >= target:
            min_len = min(min_len, right - left + 1)

            window_sum -= nums[left]
            left += 1

    return 0 if min_len > len_nums else min_len


print(min_sub_array_len(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
# print(min_sub_array_len(target=7, nums=[2, 3, 1, 2, 4, 3]))
