def find_champion(grid: list[list[int]]) -> int:
    results = {}
    for i, nums in enumerate(grid):
        results[i] = sum(nums)
    max_ = max(results.values())
    for i, numbers in enumerate(grid):
        if sum(numbers) == max_:
            return i


print(find_champion([[0, 1], [0, 0]]))
