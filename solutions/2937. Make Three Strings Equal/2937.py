def find_minimum_operations(s1: str, s2: str, s3: str) -> int:
    s1_len = len(s1)
    s2_len = len(s2)
    s3_len = len(s3)
    min_len = min(s1_len, s2_len, s3_len)
    j = 0
    for i in range(min_len):
        if s1[i] == s2[i] == s3[i]:
            j += 1
        elif i == 0:
            return -1
        else:
            break
    return s1_len + s2_len + s3_len - 3 * j


print(find_minimum_operations("abc", "abb", "ab"))
