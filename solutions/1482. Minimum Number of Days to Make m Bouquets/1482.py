def min_days(bloomDay: list[int], m: int, k: int) -> int:
    def can_make_bouquets(bloomDay: list[int], m: int, k: int, day: int) -> bool:
        bouquets = 0
        consecutive = 0

        for bloom in bloomDay:
            if bloom <= day:
                consecutive += 1

                if consecutive == k:
                    bouquets += 1
                    consecutive = 0
            else:
                consecutive = 0

        return bouquets >= m

    if m * k > len(bloomDay):
        return -1

    left, right = min(bloomDay), max(bloomDay)
    answer = left

    while left <= right:
        mid = (left + right) // 2

        if can_make_bouquets(bloomDay, m, k, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


print(min_days(bloomDay=[1, 10, 3, 10, 2], m=3, k=1))
