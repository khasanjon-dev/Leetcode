def factorial(n: int):
    fact = n
    while n > 1:
        fact *= n - 1
        n -= 1
    return fact

print(factorial(5))