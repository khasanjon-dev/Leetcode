# 1
'''
result = P * N
'''


# 2
# a, b = map(int, input().split())
# result = 0
# if len(str(a)) == 1:
#     if b > 10:
#         for num in range(10, b + 1):
#             if str(num)[0] == str(num)[-1]:
#                 result += 1
#         result += 10 - a
#     else:
#         result += b + 1 - a
# else:
#     for num in range(a, b + 1):
#         if str(num)[0] == str(num)[-1]:
#             result += 1
# print(result)


# 3
# def min_and_max(numbers: list[int]) -> list[int]:
#     result = []
#     numbers.sort()
#     result.append(sum(numbers[:4]))
#     result.append(sum(numbers[1:]))
#     return result
#
#
# print(min_and_max([1, 2, 3, 4, 5]))

# 4
# def python_dict():
#     my_dict = {
#         'integer': 'butun',
#         'if': 'agar',
#         'save': 'saqlash'
#     }
#     key = input("KALIT SO'Z KIRITING: ")
#     if res := my_dict.get(key, None):
#         print(res)
#     else:
#         print("Bunday so'z mavjud emas")
#
# python_dict()

# 5
# x1, y1, x2, y2 = map(int, input().split())
# result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# print(result)
