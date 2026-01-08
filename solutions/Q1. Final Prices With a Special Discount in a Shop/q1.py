def final_prices(prices: list[int]) -> list[int]:
    answer = prices[:]
    stack = []

    for i in range(len(prices)):
        while stack and prices[stack[-1]] >= prices[i]:
            answer[stack.pop()] -= prices[i]
        stack.append(i)
    return answer



print(final_prices([8, 4, 6, 2, 3]))
