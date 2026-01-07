def exclusive_time(n: int, logs: list[str]) -> list[int]:
    result = [0] * n
    stack = []
    prev_time = 0
    for log in logs:
        func_id, sign, time_s = log.split(":")
        func_id, time_s = int(func_id), int(time_s)
        if sign == "start":
            if stack:
                result[stack[-1]] += time_s - prev_time
            stack.append(func_id)
            prev_time = time_s
        else:
            result[stack.pop()] += time_s - prev_time + 1
            prev_time = time_s + 1
    return result


print(exclusive_time(n=2, logs=["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))
# Output: [3,4]
