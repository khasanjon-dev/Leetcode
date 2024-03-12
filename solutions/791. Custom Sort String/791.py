def custom_sort_string(order: str, s: str) -> str:
    s_list = list(s)
    for i, word in enumerate(order):
        if word in s:
            s_list.remove(word)
            s_list.insert(i, word)
    return ''.join(s_list)


print(custom_sort_string("kqep", "pekeq"))
