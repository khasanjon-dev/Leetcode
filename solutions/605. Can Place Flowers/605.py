def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    flowerbed_len = len(flowerbed)
    for i in range(flowerbed_len):

        if flowerbed[i] == 0:
            left = (i == 0) or (flowerbed[i - 1] == 0)
            right = (i == flowerbed_len - 1) or (flowerbed[i + 1] == 0)
            if left and right:
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True
    return True if n == 0 else False


print(can_place_flowers([1, 0, 0, 0, 1, 0, 0], 2))
# print(can_place_flowers([1, 0, 0, 0, 1], 1))
# print(can_place_flowers([1, 0, 0, 0, 1], 2))
# print(can_place_flowers([1, 0, 0, 0, 0, 0, 1], 2))
# print(can_place_flowers([1, 0, 0, 0, 0, 1], 2))
# print(can_place_flowers([0, 0, 1, 0, 1], 1))
