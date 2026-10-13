def smallest_divisor(nums: list[int], threshold: int) -> int:
    def is_valid(nums: list[int], threshold: int, divisor: int) -> bool:
        total_sum = 0

        for num in nums:
            total_sum += (num + divisor - 1) // divisor

        return total_sum <= threshold

    left, right = 1, max(nums)
    answer = right

    while left <= right:
        mid = (left + right) // 2

        if is_valid(nums, threshold, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


print(smallest_divisor(nums=[1, 2, 5, 9], threshold=6))
