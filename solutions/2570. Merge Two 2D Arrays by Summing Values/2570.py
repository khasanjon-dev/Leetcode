def merge_arrays(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    merge_dict = {}
    for key, value in nums1:
        merge_dict[key] = value
    for key, value in nums2:
        if merge_dict.get(key, None):
            merge_dict[key] += value
        else:
            merge_dict[key] = value
    return [[key, value] for key, value in sorted(merge_dict.items())]


print(merge_arrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]))
