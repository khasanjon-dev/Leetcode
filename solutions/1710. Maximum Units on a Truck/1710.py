def maximum_units(boxTypes: list[list[int]], truckSize: int) -> int:
    max_size = 0
    boxTypes.sort(key=lambda row: row[-1], reverse=True)
    i = 0
    for row in boxTypes:
        if row[0] <= truckSize:
            truckSize -= row[0]
            max_size += row[0] * row[1]
        else:
            max_size += truckSize * row[1]
            break
        i += 1
    return max_size


print(maximum_units([[1, 3], [5, 5], [2, 5], [4, 2], [4, 1], [3, 1], [2, 2], [1, 3], [2, 5], [3, 2]], 35))
