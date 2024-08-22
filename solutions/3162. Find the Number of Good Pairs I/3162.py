def number_of_pairs(nums1: list[int], nums2: list[int], k: int) -> int:
    pairs = sum(sum(1 for num2 in nums2 if num1 % (num2 * k) == 0) for num1 in nums1)
    return pairs


print(number_of_pairs([1, 3, 4], [1, 3, 4], 1))
