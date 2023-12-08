def fun(details: list[str]) -> int:
    result = 0
    for detail in details:
        res = detail[11:-2]
        if int(res) > 60:
            result += 1
    return result


print(fun(["5612624052M0130", "5378802576M6424", "5447619845F0171", "2941701174O9078"]))
