def busy_student(startTime: list[int], endTime: list[int], queryTime: int) -> int:
    result = 0
    for i in range(len(startTime)):
        if queryTime in range(startTime[i], endTime[i] + 1):
            result += 1
    return result


print(busy_student([4], [4], 4))
