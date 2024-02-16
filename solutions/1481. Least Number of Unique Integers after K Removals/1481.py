from collections import Counter


def find_least_num_of_unique_ints(arr: list[int], k: int) -> int:
    counts = Counter(arr)
    sort_nums = sorted(counts.items(), key=lambda num: num[1])
    res = []
    for num, count in sort_nums:
        res.extend([num] * count)
    return len(set(res[k:]))


arr = [24, 119, 157, 446, 251, 117, 22, 168, 374, 373, 323, 311, 441, 213, 120, 412, 200, 236, 328, 24, 164, 104, 331,
       32, 19, 223, 89, 114, 152, 82, 456, 381, 355, 343, 157, 245, 443, 368, 229, 49, 82, 16, 373, 142, 240, 125, 8]
k = 41
print(find_least_num_of_unique_ints(arr, k))
