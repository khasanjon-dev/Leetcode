def sum_indices_with_k_set_bits(nums: list[int], k: int) -> int:
    return sum([nums[i] for i in range(len(nums)) if k == bin(i).count('1')])


print(sum_indices_with_k_set_bits([5, 10, 1, 5, 2], 1))
