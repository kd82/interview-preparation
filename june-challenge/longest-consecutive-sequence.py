from typing import DefaultDict, List

def longestConsecutive(nums: List[int]) -> int:     
        dp = DefaultDict(int)
        for n in nums:
            dp[n] = 1
        ans = 0
        for x in dp:
            if x - 1 not in dp:
                y = x
                while y in dp:
                    y += 1
                ans = max(ans, y - x)
        return ans