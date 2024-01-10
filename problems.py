def count_bits(n: int) -> list[int]:
    return [bin(num)[2:].count('1') for num in range(n + 1)]


print(count_bits(5))
