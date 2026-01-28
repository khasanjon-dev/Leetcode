from string import ascii_lowercase, ascii_uppercase


def longest_nice_substring(s: str) -> str:
    n = len(s)
    best = ""

    for i in range(n):
        lower = set()
        upper = set()

        for j in range(i, n):
            c = s[j]
            if c.islower():
                lower.add(c)
            else:
                upper.add(c.lower())

            if lower == upper:
                sub = s[i : j + 1]
                if len(sub) > len(best):
                    best = sub

    return best


print(longest_nice_substring("YazaAay"))
