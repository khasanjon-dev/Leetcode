def reformat_number(number: str) -> str:
    numbers = number.replace(' ', '')
    numbers = numbers.replace('-', '')
    result = ''
    while len(numbers) > 4:
        result += numbers[:3] + '-'
        numbers = numbers[3:]
    if len(numbers) == 4:
        result += numbers[:2] + '-' + numbers[2:]
    else:
        result += numbers
    return result


print(reformat_number("1-23-45 6"))
