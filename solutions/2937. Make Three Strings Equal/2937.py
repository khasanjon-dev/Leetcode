def find_minimum_operations(s1: str, s2: str, s3: str) -> int:
    s1_len = len(s1)
    s2_len = len(s2)
    s3_len = len(s3)
    min_len = min(s1_len, s2_len, s3_len)
    i = 0
    while i < min_len and s1[i] == s2[i] == s3[i]:
        i += 1
    return s1_len + s2_len + s3_len - 3 * i if i != 0 else -1


print(find_minimum_operations("abc", "abb", "ab"))
