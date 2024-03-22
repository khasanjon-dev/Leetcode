def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    result = []
    for num1 in nums1:
        check = False
        for num2 in nums2:
            if num1 == num2:
                check = True
            if check:
                if num1 < num2:
                    result.append(num2)
                    break
        else:
            result.append(-1)
    return result


print(next_greater_element([4, 1, 2], [1, 3, 4, 2]))
