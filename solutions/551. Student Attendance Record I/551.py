def check_record(s: str) -> bool:
    return s.count("A") <= 1 and "LLL" not in s


print(check_record("PPALLP"))
