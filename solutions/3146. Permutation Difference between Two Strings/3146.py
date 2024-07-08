def find_permutation_difference(s: str, t: str) -> int:
    result = 0
    for i in range(len(s)):
        result += abs(i - t.index(s[i]))
    return result


print(find_permutation_difference('abc', 'bac'))
