def fun(num: str) -> str:
    res = ''
    for i in range(1, len(num) + 1):
        if int(num[-i]) % 2:
            if i == 1:
                return num
            return num[:-(i - 1)]
    return res


print(fun('4206'))
