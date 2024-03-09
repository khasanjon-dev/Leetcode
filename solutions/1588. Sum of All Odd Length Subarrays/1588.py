def sum_odd_length_sub_arrays(arr: list[int]) -> int:
    result = 0
    len_arr = len(arr)
    for i in range(0, len_arr + 1, 2):
        for j in range(len_arr - i):
            result += sum(arr[j: i + j + 1])
    return result


print(sum_odd_length_sub_arrays([1, 2]))
