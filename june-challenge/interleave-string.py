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
def interleave(s1, s2, s3):
    m, n = len(s1), len(s2)
    if m + n != len(s3): return False
    dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0: # both are empty
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
            else:
                dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1] or dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
    return dp[m][n]