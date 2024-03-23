def answer_queries(nums: list[int], queries: list[int]) -> list[int]:
    result = []
    nums.sort()
    for query in queries:
        sum_num = []
        for num in nums:
            if sum(sum_num) + num <= query:
                sum_num.append(num)
            else:
                result.append(len(sum_num))
                break
        else:
            result.append(len(sum_num))
    return result


print(answer_queries([2, 3, 4, 5], [1]))
