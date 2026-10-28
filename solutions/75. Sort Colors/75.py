def sort_colors(nums: list[int]) -> None:
    n = len(nums)

    for i in range(n - 1):

        for j in range(n - i - 1):

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

