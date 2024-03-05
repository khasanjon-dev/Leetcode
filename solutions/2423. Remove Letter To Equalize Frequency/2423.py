from collections import Counter


def equal_frequency(word: str) -> bool:
    count_list = list(Counter(word).values())
    max_ = max(count_list)
    min_ = min(count_list)
    len_set = len(set(count_list))
    if len(set(word)) == 1:
        return True
    if count_list.count(max_) == 1 and max_ - min_ == 1 and len_set == 2:
        return True
    elif max_ == min_ == 1:
        return True
    elif count_list.count(min_) == 1 and min_ - 1 == 0 and len_set == 2:
        return True
    return False


print(equal_frequency("zz"))
