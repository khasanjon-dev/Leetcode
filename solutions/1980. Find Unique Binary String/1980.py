from itertools import product


def find_different_binary_string(nums: list[str]) -> str:
    n = len(nums)
    for comb in product("01", repeat=n):
        match = "".join(comb)
        if match not in nums:
            return match



print(find_different_binary_string(["00", "01"]))
