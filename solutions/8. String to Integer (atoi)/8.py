def my_atoi(s: str) -> int:
    number = ''
    char = ''
    for num in s:
        if num.isdigit():
            if char:
                number = ''
                break
            number += num
        elif num == '-':
            if not number:
                number += '-'
        elif num.isalpha():
            char += num
    return int(number) if number else 0


print(my_atoi('42'))
