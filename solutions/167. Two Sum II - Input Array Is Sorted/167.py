def two_sum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            break
        elif current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
    return [left + 1, right + 1]


print(two_sum(numbers=[2, 7, 11, 15], target=9))
