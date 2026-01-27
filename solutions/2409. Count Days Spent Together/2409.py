def count_days_together(
    arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
) -> int:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def days_in_year(date: str) -> int:
        month, day = map(int, date.split("-"))
        return sum(days_in_month[: month - 1]) + day

    arrive_alice = days_in_year(arriveAlice)
    leave_alice = days_in_year(leaveAlice)
    arrive_bob = days_in_year(arriveBob)
    leave_bob = days_in_year(leaveBob)

    start = max(arrive_alice, arrive_bob)
    end = min(leave_alice, leave_bob)
    return max(0, end - start - 1)


print(
    count_days_together(
        arriveAlice="03-08", leaveAlice="11-28", arriveBob="01-01", leaveBob="12-31"
    )
)
