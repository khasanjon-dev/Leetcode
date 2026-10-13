def ship_within_days(weights: list[int], days: int) -> int:
    def is_enough(weights: list[int], capacity: int) -> bool:
        temp_days = 1
        temp_capacity = 0

        for weight in weights:

            if weight + temp_capacity > capacity:
                temp_days += 1
                temp_capacity = 0
                temp_capacity += weight
            else:
                temp_capacity += weight

        return temp_days <= days

    left, right = max(weights), sum(weights)
    answer = left

    while left <= right:
        mid = (left + right) // 2

        if is_enough(weights, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


print(ship_within_days(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))
