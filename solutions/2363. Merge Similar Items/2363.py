def merge_similar_items(items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
    result = []
    items_dict = {}
    for i in range(len(items1)):
        value = items1[i][0]
        weight = items1[i][1]
        items_dict[value] = weight
    for i in range(len(items2)):
        value = items2[i][0]
        weight = items2[i][1]
        value_item = items_dict.get(value, None)
        if value_item is not None:
            items_dict[value] += weight
        else:
            items_dict[value] = weight
    for key, value in items_dict.items():
        result.append([key, value])
    result.sort()
    return result


print(merge_similar_items([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]))
