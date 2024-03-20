def final_prices(prices: list[int]) -> list[int]:
    result = []
    for i, price in enumerate(prices):
        for j in range(i + 1, len(prices)):
            if prices[i] >= prices[j]:
                result.append(prices[i] - prices[j])
                break
        else:
            result.append(prices[i])
    return result


print(final_prices([10, 1, 1, 6]))
