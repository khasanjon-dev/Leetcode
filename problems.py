def number_of_employees_who_met_target(hours: list[int], target: int) -> int:
    count = 0
    for hour in hours:
        if hour >= target:
            count += 1
    return count


