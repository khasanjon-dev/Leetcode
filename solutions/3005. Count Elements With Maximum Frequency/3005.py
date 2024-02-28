def max_frequency_elements(nums: list[int]) -> int:
    counter = {}
    count = 0
    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    max_ = 1
    for num in counter.values():
        if num > max_:
            max_ = num
    for key, value in counter.items():
        if value == max_:
            count += 1
    return max_ * count


print(max_frequency_elements([1, 2, 3, 4, 5]))
