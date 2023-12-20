def buy_choco(prices: list[int], money: int) -> int:
    sort_price = sorted(prices)
    min_1, min_2 = sort_price[0], sort_price[1]
    if min_1 + min_2 <= money:
        return money - (min_2 + min_1)
    return money


print(buy_choco([3, 2, 3], 3))
