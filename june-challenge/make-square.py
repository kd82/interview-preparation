from collections import List
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def dfs(i):
            if i == len(matchsticks):
                return s[0] == s[1] == s[2] == side
            for j in range(4):
                if matchsticks[i] + s[j] > side: # if adding this side to our current sum exceeds the possible side
                    continue # do not add keep going.
                s[j] += matchsticks[i]
                if dfs(i + 1):
                    return True
                s[j] -= matchsticks[i]
            return False
        if not matchsticks:
            return False
        perm = sum(matchsticks)
        side = perm//4
        if side * 4 != perm:
            return False
        matchsticks.sort(reverse = True)
        s = [0]*4
        return dfs(0)
"""
1. Reduce the global call stack and memory foot print by using a class level variable 
2. Think logically in terms of recursion and do pruning if needed. like for example would it make sense
to add an element if not just skip it and move on
"""