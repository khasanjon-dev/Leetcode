def maximum_odd_binary_number(s: str) -> str:
    one = s.count('1')
    zero = s.count('0')
    result = ''
    result += '1' * (one - 1)
    result += '0' * zero
    result += '1'
    return result


print(maximum_odd_binary_number('0101'))
