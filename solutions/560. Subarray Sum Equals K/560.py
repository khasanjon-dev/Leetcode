def subarray_sum(nums: list[int], k: int) -> int:
    count = 0

    for i in range(len(nums)):
        sum_ = 0

        for j in range(i, len(nums)):
            sum_ += nums[j]

            if sum_ == k:
                count += 1



    return count


print(subarray_sum(nums=[1, 2, 1, 2, 1], k=3))


