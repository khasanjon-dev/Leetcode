from collections import Counter


def max_frequency_elements(nums: list[int]) -> int:
    counter = Counter(nums)
    max_ = max(counter.values())
    count = 0
    for key, value in counter.items():
        if value == max_:
            count += 1

    return max_ * count


print(max_frequency_elements([1, 2, 3, 4, 5]))
