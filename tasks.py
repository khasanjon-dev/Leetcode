# 1
# def reverse(s: str) -> str:
#     return s[::-1]
#
#
# print(reverse('HELLO, WORLD!'))

# 2
# def count_num(numbers: list[int]) -> dict:
#     result = {}
#
#     number_s = sorted(list(set(numbers)))
#     for num in number_s:
#         res = 0
#         for n in numbers:
#             if num == n:
#                 res += 1
#         result[num] = res
#     return result
#
#
# print(count_num([1, 2, 3, 2, 1, 3, 2, 4, 5, 4]))
# 3
# def find_second_max(numbers: list[int]) -> int:
#     return sorted(numbers)[-2]
#
#
# print(find_second_max([10, 5, 8, 20, 3]))
# 4
# def remove_duplicate(numbers: list[int]) -> list[int]:
#     result = []
#     for num in numbers:
#         if num not in result:
#             result.append(num)
#     return result
#
#
# print(remove_duplicate([1, 2, 3, 2, 1, 3, 2, 4, 5, 4]))

# 5
# def small_positive_number(A):
#     max_num = max(A)
#     if max_num > 0:
#         for num in range(1, max_num + 2):
#             if num not in A:
#                 return num
#     else:
#         return 1
#
#
# print(small_positive_number([-1, -3]))