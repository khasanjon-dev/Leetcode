def thousand_seperator(n: int) -> str:
    str_n = str(n)
    parts = []
    while str_n:
        parts.append(str_n[-3:])
        str_n = str_n[:-3]
    return ".".join(parts[::-1])


print(thousand_seperator(123456789))

