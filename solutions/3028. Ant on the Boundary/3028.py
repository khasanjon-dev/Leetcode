def return_to_boundary_count(nums: list[int]) -> int:
    count = 0
    steps = []
    for num in nums:
        steps.append(num)
        if sum(steps) == 0:
            count += 1
    return count


print(return_to_boundary_count([3, 2, -3, 4]))
