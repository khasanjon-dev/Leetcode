def fib(n: int) -> int:
    if n < 2:
        return n
    x, y = 0, 1
    for _ in range(2, n + 1):
        x, y = y, x + y
    return y


print(fib(2))
