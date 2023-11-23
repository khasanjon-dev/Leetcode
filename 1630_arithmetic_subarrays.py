def check_arithmetic_sub_arrays(nums: list[int], l: list[int], r: list[int]):
    result = []
    for j in range(len(l)):
        nums_cut = nums[l[j]: r[j] + 1]
        res = abs(abs(nums_cut[1]) - abs(nums_cut[0]))
        for k in range(len(nums_cut)):
            for l in range(1, len(nums_cut)):
                if res != abs(abs(nums_cut[l]) - abs(nums_cut[k])):
                    result.append(False)
                    break
        else:
            result.append(True)
    return result


nums = [-3, -6, -8, -4, -2, -8, -6, 0, 0, 0, 0]
l = [5, 4, 3, 2, 4, 7, 6, 1, 7]
r = [6, 5, 6, 3, 7, 10, 7, 4, 10]
# Output: [true,false,true]
print(check_arithmetic_sub_arrays(nums, l, r))
