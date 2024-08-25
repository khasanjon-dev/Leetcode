def can_alice_win(nums: list[int]) -> bool:
    nums.sort()
    set_nums = 0
    for i, num in enumerate(nums):
        if num > 9:
            return True if set_nums != sum(nums[i:]) else False
        else:
            set_nums += num
    return True


print(can_alice_win([3, 3, 7, 9, 4, 55, 9, 9, 13, 7, 9, 8]))
