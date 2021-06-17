from collections import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def dfs(index):
            if index == l:
                for i in range(k):
                    if s[i] != side:
                        return False
                return True
            for j in range(k):
                if s[j] + nums[index] <= side:
                    s[j] += nums[index]
                    if dfs(index + 1):
                        return True
                    s[j] -= nums[index]
            return False
        total = sum(nums)
        l = len(nums)
        if total % k != 0:
            return False
        side = total//k
        s = [0 for _ in range(k)]
        nums.sort(reverse = True)
        return dfs(0)