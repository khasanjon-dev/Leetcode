def is_trionic(nums: list[int]) -> bool:
    n = len(nums)
    i = 0
    while i + 1 < n and nums[i] < nums[i + 1]:
        i += 1
    if i == 0 or i == n - 1:
        return False
    p = i
    while i + 1 < n and nums[i] > nums[i + 1]:
        i += 1
    if i == p or i == n - 1:
        return False
    q = i
    while i + 1 < n and nums[i] < nums[i + 1]:
        i += 1
    return i > q and i == n - 1


print(is_trionic([2, 1, 3]))
