def count_good_sub_strings(s: str) -> int:
    result = 0
    for i in range(len(s)):
        if 3 == len(set(s[i: i + 3])):
            result += 1
    return result


print(count_good_sub_strings('aababcabc'))
