def find_relative_ranks(score: list[int]) -> list[str]:
    score_sort = sorted(score, reverse=True)
    result = []
    data = {
        1: 'Gold Medal',
        2: 'Silver Medal',
        3: 'Bronze Medal'
    }
    for num in score:
        index = score_sort.index(num)  + 1
        if index in data.keys():
            result.append(data[index])
        else:
            result.append(str(index))
    return result


find_relative_ranks([10, 3, 8, 9, 4])
