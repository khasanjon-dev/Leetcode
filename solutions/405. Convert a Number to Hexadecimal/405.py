def to_hex(num: int) -> str:
    if num == 0:
        return "0"

    num &= 0xFFFFFFFF

    hex_chars = "0123456789abcdef"
    result = []

    while num > 0:
        remainder = num % 16
        result.append(hex_chars[remainder])
        num //= 16

    return "".join(reversed(result))


print(to_hex(26))
