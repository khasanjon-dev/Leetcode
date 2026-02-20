def count_prime_set_bits(left: int, right: int) -> int:
    primes = {2, 3, 5, 7, 11, 13, 17, 19}

    return sum(1 for num in range(left, right + 1) if bin(num).count("1") in primes)


print(count_prime_set_bits(10, 15))
