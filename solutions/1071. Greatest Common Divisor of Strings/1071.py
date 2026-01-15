def gc_of_strings(str1: str, str2: str) -> str:
    for i in range(len(str2), 0, -1):
        str1_list = str1.split(str2[:i])
        str2_list = str2.split(str2[:i])
        if set(str1_list) == {""} and set(str2_list) == {""}:
            return str2[:i]
    return ""


print(gc_of_strings("ABABAB", "ABAB"))
