def find_minimum_operations(s1: str, s2: str, s3: str) -> int:
    j = 0
    for i, s in enumerate(zip(s1, s2, s3)):
        if len(set(s)) == 1:
            j += 1
        elif i == 0:
            return -1
        else:
            break
    return len(s1) + len(s2) + len(s3) - 3 * j


print(find_minimum_operations("abc", "abb", "ab"))
