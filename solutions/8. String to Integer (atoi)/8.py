def my_atoi(s: str) -> int:
    sign = 1
    s = s.strip()
    if not s:
        return 0
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    result = 0
    for char in s:
        if not char.isdigit():
            break
        digit = int(char)
        result = result * 10 + digit
        if sign == 1 and result >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif sign == -1 and result >= 2 ** 31:
            return -2 ** 31
    return sign * result


print(my_atoi("+-12"))
