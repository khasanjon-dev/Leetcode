def pivot_integer(n: int) -> int:
    if n == 1:
        return 1
    nums = [x for x in range(1, n + 1)]
    for i in range(n):
        if sum(nums[:i + 1]) == sum(nums[i:]):
            return nums[i]
    return -1


print(pivot_integer(4))
