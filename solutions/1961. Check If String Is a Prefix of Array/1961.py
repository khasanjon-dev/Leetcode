def is_prefix_string(s: str, words: list[str]) -> bool:
    s_len = len(s)
    temp = ""
    for word in words:
        temp += word
        if len(temp) >= s_len:
            return temp == s
    return False


print(is_prefix_string("iloveleetcode", ["apples", "i", "love", "leetcode"]))
