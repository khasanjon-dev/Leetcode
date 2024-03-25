from collections import Counter


def find_duplicates(nums: list[int]) -> list[int]:
    counter_nums = sorted(Counter(nums).items(), key=lambda item: item[-1], reverse=True)
    result = []
    for value, count in counter_nums:
        if count == 2:
            result.append(value)
        else:
            break
    return result


print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))
