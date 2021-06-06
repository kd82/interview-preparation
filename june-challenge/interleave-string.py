def isInterleave(s1: str, s2: str, s3: str) -> bool:
        def dfs(i, j, k): # dfs with memo 
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j == len(s2):
                return s1[i:] == s3[k:]
            if (i, j) in memo:
                return memo[(i, j)]
            res = False
            if s1[i] == s3[k] and dfs(i + 1, j, k + 1) or s2[j] == s3[k] and dfs(i, j + 1, k + 1):
                res = True
            memo[(i, j)] = res
            return memo[(i,j)]
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        return dfs(0, 0, 0)