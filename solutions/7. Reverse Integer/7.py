def reverse(x: int) -> int:
    str_x = str(x)
    if str_x[0] == '-':
        num = -int(str_x[1:][::-1])
    else:
        num = int(str_x[::-1])
    if num > (2 ** 31) - 1 or num < (-2 ** 31):
        return 0
    return num


print(reverse(-123))
# print(2 ** 31 - 1 < 9646324351)
