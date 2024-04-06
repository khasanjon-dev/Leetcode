def find_the_array_conc_val(nums: list[int]) -> int:
    result = 0
    while nums:
        num_1_str = str(nums.pop(0))
        num_2_str = ''
        if nums:
            num_2_str = str(nums.pop())

        result += int(num_1_str + num_2_str)
    return result


print(find_the_array_conc_val([7, 52, 2, 4]))
