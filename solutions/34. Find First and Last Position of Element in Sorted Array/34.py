def search_range(nums: list[int], target: int) -> list[int]:
    def find_first(nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                answer = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return answer

    def find_last(nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                answer = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return answer
    return [find_first(nums, target), find_last(nums, target)]

print(search_range(nums=[5, 7, 7, 8, 8, 10], target=8))
