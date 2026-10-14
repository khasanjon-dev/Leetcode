def find_max_average(nums: list[int], k: int) -> float:
    temp_sum = sum(nums[:k])
    answer = temp_sum

    for right in range(k, len(nums)):
        temp_sum -= nums[right - k]
        temp_sum += nums[right]
        answer = max(answer, temp_sum)

    return answer / k


print(find_max_average(nums=[1, 12, -5, -6, 50, 3], k=4))
