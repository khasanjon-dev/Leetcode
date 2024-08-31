def repeated_character(s: str) -> str:
    len_s = len(s)
    for i in range(len_s - 1):
        if s[i] == s[i + 1]:
            return s[i]
    for i in range(len_s):
        for j in range(i + 1, len_s):
            if s[i] == s[j]:
                return s[i]


print(repeated_character("nwcn"))
