from typing import List
def minCost(costs: List[List[int]]) -> int:
        def paintHelper(costs, i, color): #bruteforce
            if len(costs) == i:
                return 0
            minCost = costs[i][color]
            if color == 0:
                minCost += min(paintHelper(costs, i + 1, 1), paintHelper(costs, i + 1, 2))
            elif color == 1:
                minCost += min(paintHelper(costs, i + 1, 0), paintHelper(costs, i + 1, 2))
            else:
                minCost += min(paintHelper(costs, i + 1, 0), paintHelper(costs, i + 1, 1))
            return minCost
        if len(costs) == 0:
            return 0
        return min(paintHelper(costs, 0, 0), paintHelper(costs, 0, 1), paintHelper(costs, 0, 2))