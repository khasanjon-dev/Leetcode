def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                temp = [nums[i], nums[left], nums[right]]
                if not temp in result:
                    result.append(temp)
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


print(three_sum([-1, 0, 1, 2, -1, -4]))
