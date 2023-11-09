def split(strings: str, regex: str):
    return strings.split(regex)


print(split("ab#12#453", "#"))
