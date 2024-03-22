from itertools import chain


def find_missing_and_repeated_values(grid: list[list[int]]) -> list[int]:
    # nums = [num for num in range(1, len(grid) ** 2 + 1)]
    grid_chain = list(chain(*grid))
    result = []
    num_no = None
    for num in range(1, len(grid) ** 2 + 1):
        if num in grid_chain:
            if grid_chain.count(num) > 1:
                result.append(num)
                if num_no:
                    break
        else:
            num_no = num
    result.append(num_no)

    return result


print(find_missing_and_repeated_values([[9, 1, 7], [8, 9, 2], [3, 4, 6]]))
