# x = input()
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

    '100': 'yuz',

    '1000': 'ming',

}
print(my_dict)
# result = ''
# if len(x) >= 4:
#     if x[1] == '0' and x[2] == '0' and x[3] == '0':
#         result = my_dict[x] if x[0] == 1 else my_dict[x[0]] + ' ' + my_dict['1000']
#     elif x[1] == '0' and x[2] == '0':
#         result = my_dict[x[0]] + ' ' + my_dict['1000'] + ' ' + my_dict[x[3]]
#     elif x[2] == '0' and x[3] == '0':
#         result = my_dict[x[0]] + ' ' + my_dict['1000'] + ' ' + my_dict[x[1]] + ' ' + my_dict['100']
#     elif x[1] == '0' and x[3] == '0':
#         result = my_dict[x[0]] + ' ' + my_dict['1000'] + ' ' + my_dict[x[2] + '0']
#     elif x[1] == '0':
#         result = my_dict[x[0]] + ' ' + my_dict['1000'] + ' ' + my_dict[x[2] + '0'] + ' ' + my_dict[x[3]]
#     elif x[2] == '0':
#         result = my_dict[x[0]] + ' ' + my_dict['1000'] + ' ' + my_dict[x[1]] + ' ' + my_dict['100'] + ' ' + my_dict[
#             x[3]]
#     elif x[3] == '0':
#         result = my_dict[x[0]] + ' ' + my_dict['1000'] + ' ' + my_dict[x[1]] + ' ' + my_dict['100'] + ' ' + my_dict[
#             x[2] + '0']
#     else:
#         result = my_dict[x[0]] + ' ' + my_dict['1000'] + ' ' + my_dict[x[1]] + ' ' + my_dict['100'] + ' ' + my_dict[
#             x[2] + '0'] + ' ' + my_dict[x[3]]
# elif len(x) >= 3:
#     if x[1] == '0' and x[2] == '0':
#         result = my_dict[x] if x[0] == 1 else my_dict[x[0]] + my_dict['100']
#     elif x[-1] == '0':
#         result = my_dict[x[0]] + ' ' + my_dict['100'] + ' ' + my_dict[x[1] + '0']
#     else:
#         result = my_dict[x[0]] + ' ' + my_dict['100'] + ' ' + my_dict[x[2]] if x[1] == '0' else my_dict[x[
#             0]] + ' ' + my_dict['100'] + ' ' + my_dict[x[1] + '0'] + ' ' + my_dict[x[2]]
# elif len(x) >= 2:
#     result = my_dict[x] if x[-1] == '0' else my_dict[x[0] + '0'] + ' ' + my_dict[x[1]]
# else:
#     result = my_dict[x]
# print(result)
