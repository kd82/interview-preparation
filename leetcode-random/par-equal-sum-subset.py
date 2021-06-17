from collections import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # @lru_cache(maxsize = None) can be used to cache the results
        def dfs(index, s):
            if s == subsetSum:
                return True
            if s > subsetSum or index >= len(nums):
                return False
            return dfs(index + 1, s) or dfs(index + 1, s + nums[index])
        total = sum(nums)
        if total % 2 != 0:
            return False
        subsetSum = total//2
        return dfs(0, 0)

    def canPartition1(self, nums: List[int]) -> bool: # dp bottum up based on the 0/1 knapsack
        total = sum(nums)
        if total % 2 != 0:
            return False
        subsetSum = total//2
        n = len(nums)
        dp = [[False for _ in range(subsetSum + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(subsetSum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[n][subsetSum]