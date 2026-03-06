def check_ones_segment(s: str) -> bool:
    is_zero = False
    is_one = False
    for i, num in enumerate(s):
        if is_zero and is_one:
            if "1" in s[i:]:
                return False
        if num == "1":
            is_one = True
        else:
            is_zero = True
    return True


print(check_ones_segment("1001"))
