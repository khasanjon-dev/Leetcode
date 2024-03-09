def get_common(nums1: list[int], nums2: list[int]) -> int:
    common_datas = set(nums1).intersection(nums2)
    return min(common_datas) if common_datas else -1
