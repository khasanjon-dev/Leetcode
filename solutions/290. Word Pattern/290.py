def word_pattern(pattern: str, s: str) -> bool:
    s_list = s.split()
    if len(s_list) != len(pattern):
        return False
    pattern_w = {}
    w_pattern = {}
    for p, w in zip(pattern, s_list):
        if p in pattern_w and pattern_w[p] != w:
            return False
        if w in w_pattern and w_pattern[w] != p:
            return False
        pattern_w[p] = w
        w_pattern[w] = p
    return True


print(word_pattern("abba", "dog dog dog dog"))
