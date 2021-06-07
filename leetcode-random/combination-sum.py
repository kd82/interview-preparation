 from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(k, curr, start):
            if k < 0:
                return
            if k == 0:
                res.append(list(curr))
                return
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtrack(k - candidates[i], curr, i)
                curr.pop()
        res = []
        backtrack(target, [], 0)
        return res