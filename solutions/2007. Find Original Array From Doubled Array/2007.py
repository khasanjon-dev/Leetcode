from collections import Counter


def find_original_array(changed: list[int]) -> list[int]:
    if len(changed) % 2 != 0:
        return []
    original = []
    num_counts = Counter(changed)
    for num in sorted(changed):
        if num == 0:
            if num_counts[num] % 2 != 0:
                return []
        if num_counts[num] == 0:
            continue
        num2 = num * 2
        if num2 in num_counts and num_counts[num2] > 0:
            original.append(num)
            num_counts[num] -= 1
            num_counts[num2] -= 1
    if len(original) == len(changed) // 2:
        return original
    return []


print(find_original_array([4, 0, 3, 0]))
