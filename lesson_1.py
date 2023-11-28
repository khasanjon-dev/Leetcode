class Solution:
    def maximum_wealth(self, nums: list[list[int]]) -> int:
        # result = []
        # for num in nums:  # [1, 2, 3]
        #     result.append(sum(num))
        # return max(result)
        return max([sum(num) for num in nums])


solution = Solution()
result = solution.maximum_wealth([[1, 2, 3], [3, 2, 1]])
print(result)
