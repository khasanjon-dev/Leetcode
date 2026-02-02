def minimum_cost(nums: list[int], k: int, dist: int) -> int:
    result = nums.pop(0)
    for _ in range(k - 1):
        min_num = min(nums)
        i = nums.index(min_num)


    # write more logic here


    return result


print(minimum_cost(nums=[1, 3, 2, 6, 4, 2], k=3, dist=3))
