from collections import Counter


def custom_sort_string(order: str, s: str) -> str:
    # s_order_indexes = {}

    s_order_indexes = {}
    extra = ''
    s_counter = Counter(s)
    for key, count in s_counter.items():
        if key in order:
            s_order_indexes[order.index(key)] = key * count
        else:
            extra += key * count
    s_order = ''
    for key, value in sorted(s_order_indexes.items()):
        s_order += value
    return s_order + extra


print(custom_sort_string("jftiugkz", "kfiukutzjg"))
