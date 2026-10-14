def count_good_substring(s: str) -> int:
    count = 0
    k = 3

    for i in range(0, len(s) - k + 1):

        if len(set(s[i:i + k])) == k:
            count += 1

    return count


print(count_good_substring(s="aababcabc"))
