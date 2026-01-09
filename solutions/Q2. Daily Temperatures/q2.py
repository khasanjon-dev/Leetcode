def daily_temperatures(temperatures: list[int]) -> list[int]:
    len_temps = len(temperatures)
    result = [0] * len_temps
    stack = []
    for i in range(len_temps):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result


print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
