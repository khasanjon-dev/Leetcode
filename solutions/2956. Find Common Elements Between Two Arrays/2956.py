def find_intersection_values(nums1: list[int], nums2: list[int]) -> list[int]:
    count_1 = 0
    for num in nums1:
        if num in nums2:
            count_1 += 1
    count_2 = 0
    for num in nums2:
        if num in nums1:
            count_2 += 1
    return [count_1, count_2]


print(find_intersection_values([24, 28, 7, 27, 7, 27, 9, 24, 9, 10], [12, 29, 9, 7, 5]))
