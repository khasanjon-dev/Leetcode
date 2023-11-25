def truncate_sentence(s: str, k: int) -> str:
    strings_list = s.split()[:k]
    result = ''
    for word in strings_list:
        result += word + ' '
    return result.strip()


s = "Hello how are you Contestant"
k = 4
# result
# "Hello how are you"
print(truncate_sentence(s, k))
