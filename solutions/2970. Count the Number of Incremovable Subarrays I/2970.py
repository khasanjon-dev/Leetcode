def incremovable_subarray_count(nums: list[int]) -> int:
    n = len(nums)
    count = 0
    for l in range(n):
        for r in range(l, n):
            prev = -1
            valid = True
            for i in range(n):
                if l <= i <= r:
                    continue
                if nums[i] <= prev:
                    valid = False
                    break
                prev = nums[i]
            if valid:
                count += 1
    return count


print(incremovable_subarray_count([1, 2, 3, 4]))
