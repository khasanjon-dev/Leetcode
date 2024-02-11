def kth_distinct(arr: list[str], k: int) -> str:
    res = []
    for i in range(len(arr)):
        if arr[i] not in arr[:i] and arr[i] not in arr[i + 1:]:
            res.append(arr[i])
    if len(res) >= k:
        return res[k - 1]
    return ''


arr = ["aaa", "aa", "a"]
print(kth_distinct(arr, 1))


def kth_distinct(arr: list[str], k: int) -> str:
    result = []
    for word in arr:
        if arr.count(word) == 1:
            result.append(word)
    if len(result) >= k:
        return result[k - 1]
    return ''


arr = ["aaa", "aa", "a"]
print(kth_distinct(arr, 1))
