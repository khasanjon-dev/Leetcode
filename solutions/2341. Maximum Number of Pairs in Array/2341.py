from collections import Counter


def number_of_pairs(nums: list[int]) -> list[int]:
    nums_counter = Counter(nums)
    count_pair = 0
    count_num = 0
    for key, value in nums_counter.items():
        if value // 2 > 0:
            if value % 2 == 1:
                count_num += 1
            count_pair += value // 2
        else:
            count_num += 1
    return [count_pair, count_num]


print(number_of_pairs([1, 3, 2, 1, 3, 2, 2]))
