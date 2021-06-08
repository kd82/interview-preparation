from collections import List

def minCostClimbingStairs(cost: List[int]) -> int:
    def dfs(cost, i):
        if i >= len(cost):
            return 0
        if dp[i] > -1:
            return dp[i]
        res = cost[i] + min(dfs(cost, i + 1), dfs(cost, i + 2))
        dp[i] = res
        return res
    dp = [-1]*(len(cost))
    return min(dfs(cost, 0), dfs(cost, 1))

def dfsbu(cost):
    d1, d2 = 0, 0
    for i in range(2, len(cost) + 1):
        temp = d1
        d1 = min(cost[i - 1] + d1, cost[i - 2] + d2)
        d2 = temp 
    return d1