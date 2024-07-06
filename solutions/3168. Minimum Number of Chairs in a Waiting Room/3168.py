def minimum_chairs(s: str) -> int:
    max_chairs = []
    max_chair = 0
    for w in s:
        if w == 'E':
            max_chair += 1
        elif w == 'L':
            if max_chair >= 1:
                max_chair -= 1
        max_chairs.append(max_chair)
    return max(max_chairs)


print(minimum_chairs('ELEELEELLL'))
