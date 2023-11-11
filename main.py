my_dict = {
    '1': 'bir',

    '2': 'ikki',

    '3': 'uch',

    '4': 'to’rt',

    '5': 'besh',

    '6': 'olti',

    '7': 'yetti',

    '8': 'sakkiz',

    '9': 'to’qqiz',
    '10': 'o’n',

    '20': 'yigirma',

    '30': 'o’ttiz',

    '40': 'qirq',

    '50': 'ellik',

    '60': 'oltmish',

    '70': 'yetmish',

    '80': 'sakson',

    '90': 'to’qson',

    '100': 'bir yuz',

    '1000': 'bir ming',

}
# input 59
# output 'besh yuz to'qson besh' # noqa
x = input()
result = ''
if len(x) >= 4:
    result += my_dict[x[0]] + ' ming ' + my_dict[x[1]] + ' yuz ' + my_dict[x[2]] + "o'n " + my_dict[x[3]]
elif len(x) >= 3:
    result += my_dict[x[0]] + ' yuz ' + my_dict[x[1]] + "o'n " + my_dict[x[2]]
elif len(x) >= 2:
    result += my_dict[x[0] + '0'] + ' ' + my_dict[x[1]]
else:
    result = my_dict[x]
print(result)
