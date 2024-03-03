def min_number(nums1: list[int], nums2: list[int]) -> int:
    equalities = []
    for num in nums1:
        if num in nums2:
            equalities.append(num)
    min1 = min(nums1)
    min2 = min(nums2)
    min_num = int(str(min1) + str(min2)) if min1 < min2 else int(str(min2) + str(min1))
    if equalities:
        return min_num if min_num <= min(equalities) else min(equalities)
    return min_num


print(min_number([4, 1, 3], [5, 7]))
