def find_complement(num: int) -> int:
    mask = (1 << num.bit_length()) - 1
    return num ^ mask

print(find_complement(5))