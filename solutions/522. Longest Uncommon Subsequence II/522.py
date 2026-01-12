def fin_lus_length(strs: list[str]) -> int:
    strs.sort(key=len, reverse=True)

    def is_subsequence(a, b):
        i = 0
        len_a = len(a)
        for s in b:
            if i < len_a and a[i] == s:
                i += 1
        return i == len_a

    len_strs = len(strs)
    max_length = -1
    for i in range(len_strs):
        for j in range(len_strs):
            if i != j:
                if is_subsequence(strs[i], strs[j]):
                    break
        else:
            return len(strs[i])
    return max_length


print(fin_lus_length(["aaa", "aaa", "aa"]))
