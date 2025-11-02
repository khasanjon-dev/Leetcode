def arrange_coins(n: int) -> int:
    count = 0
    while n >= count + 1:
        count += 1
        n -= count
    return count


print(arrange_coins(3))  # 2
print(arrange_coins(8))  # 3
print(arrange_coins(5))  # 2
print(arrange_coins(1))  # 1
print(arrange_coins(2))  # 1
print(arrange_coins(4))  # 2
