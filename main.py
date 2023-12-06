from string import ascii_lowercase as lower_let


def replace_digits(s: str) -> str:
    result = ''
    for i, w in enumerate(s):
        if w.isdigit():
            result += lower_let[lower_let.index(s[i - 1]) + int(w)]
        else:
            result += w
    return result


print(replace_digits('a1b2c3d4e'))
