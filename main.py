def int_to_roman(num: int) -> str:
    num_s = str(num)
    roman_numbers = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }
    pass


print(int_to_roman(3))
'''
125
V
XX
C
CXXV
'''