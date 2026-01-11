def find_lus_length(a: str, b: str) -> int:
    return max(len(a), len(b)) if a != b else -1


print(find_lus_length("aefawfawfawfaw", "aefawfeawfwafwaef"))
