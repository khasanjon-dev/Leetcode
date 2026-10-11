def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed not in seen:
            seen[num] = i
        else:
            return [seen[needed], i]


print(two_sum(nums=[3, 2, 4], target=6))
