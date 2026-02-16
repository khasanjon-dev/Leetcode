from datetime import date


def day_of_the_week(day: int, month: int, year: int) -> str:
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    d = date(year, month, day)
    return days[d.weekday()]


print(day_of_the_week(day=31, month=8, year=2019))
