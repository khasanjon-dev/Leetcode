def convert_to_base_7(num: int) -> str:
    result = ""
    is_minus = False
    if num < 0:
        num *= -1
        is_minus = True
    while num:
        residue = num % 7
        result += str(residue)
        num = num // 7
    if is_minus:
        result += "-"
    return result[::-1] if result else "0"


print(convert_to_base_7(-7))
