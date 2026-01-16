from datetime import datetime


def days_between_dates(date1: str, date2: str) -> int:
    date1 = datetime.strptime(date1, "%Y-%m-%d").date()
    date2 = datetime.strptime(date2, "%Y-%m-%d").date()
    diff = date1 - date2
    return int(diff.days)


print(days_between_dates(date1="2020-01-15", date2="2019-12-31"))
