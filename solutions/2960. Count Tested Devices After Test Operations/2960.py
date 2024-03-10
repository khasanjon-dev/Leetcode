def count_tested_devices(batteryPercentages: list[int]) -> int:
    count = 0
    for i in range(len(batteryPercentages)):
        num = batteryPercentages[i]
        if num > 0:
            count += 1
            batteryPercentages = [num - 1 if num > 0 else 0 for num in batteryPercentages]
    return count


print(count_tested_devices([1, 1, 2, 1, 3]))
