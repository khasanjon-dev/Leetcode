def maximum_unique_subarray(nums: list[int]) -> int:
    seen = set()
    right = 0
    left = 0
    max_score = 0
    temp_sum = 0
    while right < len(nums):
        if nums[right] not in seen:
            temp_sum += nums[right]
            max_score = max_score if max_score >= temp_sum else temp_sum
            seen.add(nums[right])
            right += 1
        else:
            temp_sum -= nums[left]
            seen.remove(nums[left])
            left += 1
    return max_score


nums = [4, 2, 4, 5, 6]
print(maximum_unique_subarray(nums))

# output 17
