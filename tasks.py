def fun(keys: dict) -> tuple:
    mum, math, his = {}, {}, {}
    for key, value in keys.items():
        if 1 <= int(key) <= 10:
            mum[key] = value
        elif 11 <= int(key) <= 20:
            math[key] = value
        elif 21 <= int(key) <= 30:
            his[key] = value

    return mum, math, his


keys = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'a',
    '5': 'b',
    '6': 'a',
    '12': 'b',
    '13': 'a',
    '21': 'a',
    '23': 'b',
    '26': 'a'
}
mum, math, his = fun(keys)
general = mum
general.update(math)
general.update(his)
result = ', '.join(general)
print(result)
