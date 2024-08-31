def are_number_ascending(s: str) -> bool:
    strings = s.split(" ")
    last_number = 0
    for string in strings:
        if string.isdigit():
            if int(string) <= last_number:
                return False
            last_number = int(string)
    return True


print(are_number_ascending("hello world 5 x 5"))
