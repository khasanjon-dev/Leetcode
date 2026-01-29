def have_conflict(event1: list[str], event2: list[str]) -> bool:
    start1, end1 = event1
    start2, end2 = event2

    return max(start1, start2) <= min(end1, end2)


print(have_conflict(["01:15", "02:00"], ["02:00", "03:00"]))
