def self_dividing_numbers(left: int, right: int) -> list[int]:
    result = []
    for num in range(left, right + 1):
        for n in str(num):
            if n != "0" and num % int(n) == 0:
                pass
            else:
                break
        else:
            result.append(num)
    return result


print(self_dividing_numbers(1, 22))
