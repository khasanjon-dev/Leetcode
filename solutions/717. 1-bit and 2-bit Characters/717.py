def is_one_bit_character(bits: list[int]) -> bool:
    bits_len = len(bits)
    if bits_len == 1:
        return bits[0] == 0
    if bits_len % 2:
        return (bits[-3] == 1 and (bits[-2] == 0 or bits[-2] == 1) and bits[-1] == 0) or (
                bits[-1] == bits[-2] == bits[-3] == 0)
    else:
        return bits[-1] == 0 == bits[-2]


print(is_one_bit_character([0, 0, 0, 0]), True)
print(is_one_bit_character([0, 1, 0]), False)
print(is_one_bit_character([1, 0, 0]), True)
print(is_one_bit_character([0, 0, 0]), True)
