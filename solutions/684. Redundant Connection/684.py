def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    resource = []
    result = []
    for nums in edges:
        if nums[0] in resource and nums[1] in resource:
            result.append(nums)
        else:
            resource.extend(nums)

    return result[-1] if result else nums


edges = [[1, 2], [1, 3], [2, 3]]
result = [2, 3]

edges1 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
result1 = [1, 4]

edges2 = [[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]
result2 = [1, 3]

edges3 = [[1, 3], [3, 4], [1, 5], [3, 5], [2, 3]]
result3 = [3, 5]

edges4 = [[9, 10], [5, 8], [2, 6], [1, 5], [3, 8], [4, 9], [8, 10], [4, 10], [6, 8], [7, 9]]
result4 = [4, 10]

edges5 = [[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]
result5 = [1, 3]

edges6 = [[1, 5], [3, 4], [3, 5], [4, 5], [2, 4]]
result6 = [4, 5]

print(find_redundant_connection(edges4))
