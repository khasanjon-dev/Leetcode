from collections import Counter


def sort_string(s: str) -> str:
    result = ''
    counter = Counter(s)
    asc_sort = sorted(counter.keys())
    desc_sort = sorted(counter.keys(), reverse=True)

    while counter:
        for char in asc_sort:
            if counter[char] > 0:
                result += char
                counter[char] -= 1
                if counter[char] == 0:
                    del counter[char]
        for char in desc_sort:
            if counter[char] > 0:
                result += char
                counter[char] -= 1
                if counter[char] == 0:
                    del counter[char]
    return result


s = "aaaabbbbcccc"
print(sort_string(s))
