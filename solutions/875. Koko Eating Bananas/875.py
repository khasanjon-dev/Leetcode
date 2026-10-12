def min_eating_speed(piles: list[int], h: int) -> int:
    left, right = 1, max(piles)
    answer = right

    while left <= right:
        mid = (left + right) // 2

        total_hours = sum(
            (pile + mid - 1) // mid
            for pile in piles
        )

        if total_hours <= h:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


print(min_eating_speed(piles=[3, 6, 7, 11], h=8))
