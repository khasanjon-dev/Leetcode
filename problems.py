def are_almost_equal(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    if len(s1) != len(s2):
        return False
    for j in range(len(s2)):
        for i in range(1, len(s2)):
            s3 = s2[:j] + s2[i] + s2[j + 1:i] + s2[j] + s2[i + 1:]
            if s3 == s1:
                return True
    return False


print(are_almost_equal("siyolsdcjthwsiplccjbuceoxmpjgrauocx", "siyolsdcjthwsiplccpbuceoxmjjgrauocx"))
