def fun(coordinates: str) -> bool:
    data = {
        'a': [False, True],
        'b': [True, False],
        'c': [False, True],
        'd': [True, False],
        'e': [False, True],
        'f': [True, False],
        'g': [False, True],
        'h': [True, False]
    }
    if int(coordinates[-1]) % 2:
        return data[coordinates[0]][0]
    else:
        return data[coordinates[0]][1]


print(fun('b1'))
