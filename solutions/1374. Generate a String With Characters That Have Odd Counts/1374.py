def generate_the_string(n: int) -> str:
    return 'a' * n if n % 2 else 'a' * (n - 1) + 'b'


print(generate_the_string(17))
