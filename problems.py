def rearrange_array(nums: list[int]) -> list[int]:
    positives = []
    minus = []
    for num in nums:
        if num >= 0:
            positives.append(num)
        else:
            minus.append(num)
    result = []
    while positives or minus:
        result.append(positives.pop(0))
        result.append(minus.pop(0))
    return result


print(rearrange_array([-1, 1]))
