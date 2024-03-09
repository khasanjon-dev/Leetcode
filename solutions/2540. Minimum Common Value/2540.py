def get_common(nums1: list[int], nums2: list[int]) -> int:
    nums1 = set(nums1)
    nums2 = set(nums2)
    l1 = len(nums1)
    l2 = len(nums2)
    nums = []
    if l1 >= l2:
        for num in nums2:
            if num in nums1:
                nums.append(num)
    else:
        for num in nums1:
            if num in nums2:
                nums.append(num)
    if nums:
        return min(nums)
    return -1


print(get_common([2, 4], [4, 12, 13]))
