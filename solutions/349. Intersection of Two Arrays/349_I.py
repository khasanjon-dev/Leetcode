def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    result = []
    len1 = len(nums1)
    len2 = len(nums2)
    if len1 >= len2:
        for num in nums2:
            if num in nums1 and num not in result:
                result.append(num)
        return result
    for num in nums1:
        if num in nums2 and num not in result:
            result.append(num)
    return result


print(intersection([1, 2, 2, 1], [2, 2]))
