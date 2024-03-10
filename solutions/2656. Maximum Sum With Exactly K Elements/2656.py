def maximize_sum(nums: list[int], k: int) -> int:
	return (2 * max(nums) + k - 1) * k // 2


print(maximize_sum([1, 2, 3, 4, 5], 3))
