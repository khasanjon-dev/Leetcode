def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    a = newInterval[0]
    b = newInterval[1]
    result = []
    new_row = []
    for row in intervals:
        add = True
        x = row[0]
        y = row[1]
        if x <= a and y < a:
            result.append(row)
            add = False
        if x <= a < y <= b:
            new_row.append(x)
            add = False
        if y >= b and x <= a:
            new_row.append(y)
            result.append(new_row)
            new_row = []
            add = False
        if add:
            result.append(row)
    return result


print(insert([[1, 3], [6, 9]], [2, 5]))
