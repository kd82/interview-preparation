 from typing import List
def combinationSum3(k: int, n: int) -> List[List[int]]:
        def helper(n, k, curr, start):
            if k == 0 and n == 0:
                res.append(list(curr))
                return
            if k < 0 or n < 0:
                return 
            for i in range(start, 10):
                curr.append(i)
                helper(n - i, k - 1, curr, i + 1)
                curr.pop()
        res = []
        helper(n, k, [], 1)
        return res

        """
        Key Takeaways from the question 
        1. We don't need to use the set if we can use recursive call stak 
        2. Early Exit is the key for these kind fo problems 
        3. Based on the question decide if we need to keep track of starting index for recursion
        """