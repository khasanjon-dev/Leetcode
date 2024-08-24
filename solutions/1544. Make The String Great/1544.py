def make_good(s: str) -> str:
    sign = True
    while sign:
        for i in range(len(s) - 1):
            ord_s1 = ord(s[i])
            ord_s2 = ord(s[i + 1])
            if ord_s1 - 32 == ord_s2 or ord_s1 == ord_s2 - 32:
                s = s[:i] + s[i + 2:]
                break
        else:
            sign = False

    return s

print(make_good("Pp"))
