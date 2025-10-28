def licence_key_formatting(s: str, k: int) -> str:
    s = s.replace("-", "").upper()
    len_s = len(s)
    firs_group_len = len_s % k or k
    groups = [s[:firs_group_len]]
    for i in range(firs_group_len, len_s, k):
        groups.append(s[i: i + k])
    return "-".join(groups)


response = licence_key_formatting("2-4A0r7-4k", 4)
response1 = licence_key_formatting("2-5g-3-J", 2)
print(response)
print(response1)
