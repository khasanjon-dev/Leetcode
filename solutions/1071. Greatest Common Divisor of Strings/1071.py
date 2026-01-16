from math import gcd


def gc_of_strings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    i = gcd(len(str1), len(str2))
    return str1[:i]


print(gc_of_strings("ABABAB", "ABAB"))