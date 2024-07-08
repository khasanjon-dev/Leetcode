def int_to_roman(num: int) -> str:
    romans = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }
    roman = ''
    for i, n in enumerate(str(num)[::-1], 1):
        n = int(n)
        if i == 1:
            if 1 <= n <= 3:
                roman += romans[1] * n
            if 



print(int_to_roman(3))
