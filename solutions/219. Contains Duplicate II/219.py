def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    seen = {}
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False


print(contains_nearby_duplicate(nums=[1, 2, 1, 1], k=1))
