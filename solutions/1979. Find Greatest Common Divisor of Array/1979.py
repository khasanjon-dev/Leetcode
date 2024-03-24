from math import gcd


def find_gcd(nums: list[int]) -> int:
    return gcd(max(nums), min(nums))


print(find_gcd([3, 3]))
