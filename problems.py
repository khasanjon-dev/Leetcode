from itertools import combinations


def minimum_sum(num: int) -> int:
    nums = [int(n) for n in str(num)]
    nums.sort()
    num1, num2 = nums[0], nums[1]
    num3, num4 = nums[2], nums[3]
    new_1 = int(str(min(num1, num2)) + str(max(num3, num4)))
    new_2 = int(str(max(num1, num2)) + str(min(num3, num4)))
    return new_1 + new_2

print(minimum_sum(2932))
