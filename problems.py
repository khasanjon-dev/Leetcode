def frequency_sort(s: str) -> str:
    s_count = {}
    for w in s:
        s_count[w] = s_count.get(w, 0) + 1
    sort_s = sorted(s_count.keys(), key=lambda x: s_count[x], reverse=True)
    return ''.join(w * s_count[w] for w in sort_s)


print(frequency_sort("loveleetcode"))
