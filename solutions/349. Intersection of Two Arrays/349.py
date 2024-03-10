def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1).intersection(nums2))


print(intersection([1, 2, 2, 1], [2, 2]))
