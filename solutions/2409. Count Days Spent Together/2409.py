def count_days_together(
    arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
) -> int:
    ar_a_month, ar_a_day = map(int, arriveAlice.split("-"))  # ar => arrive, a => Alice
    lv_a_month, lv_a_day = map(int, leaveAlice.split("-"))  # lv => leave, a => Alice
    ar_b_month, ar_b_day = map(int, arriveBob.split("-"))  # ar => arrive, b => Bob
    lv_b_month, lv_b_day = map(int, leaveBob.split("-"))  # lv => leave, b => Bob
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    b_range = range(ar_b_month, lv_b_month + 1)
    a_range = range(ar_a_month, lv_a_month + 1)
    print(b_range)
    print(a_range)
    if b_range in a_range:
        print("good")
    else:
        print("bad")

print(
    count_days_together(
        arriveAlice="01-01", leaveAlice="12-31", arriveBob="03-02", leaveBob="09-07"
    )
)
