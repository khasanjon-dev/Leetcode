def two_out_of_three(nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
    merge_list = []
    nums_set = set(nums1 + nums2 + nums3)
    for num in nums_set:
        if (num in nums1 and num in nums2) or (num in nums1 and num in nums3) or (num in nums2 and num in nums3):
            merge_list.append(num)
    return merge_list


print(two_out_of_three([1, 1, 3, 2], [2, 3], [3]))
