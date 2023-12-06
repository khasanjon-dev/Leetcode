def fun(num: str) -> str:
    return str(int(num[::-1]))[::-1]

print(fun('123'))
