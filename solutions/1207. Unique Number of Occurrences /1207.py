from collections import Counter


def unique_occurrences(arr: list[int]) -> bool:
    arr_counter = Counter(arr)
    return len(set(arr_counter.values())) == len(set(arr_counter))


print(unique_occurrences([1, 2, 2, 1, 1, 3]))
