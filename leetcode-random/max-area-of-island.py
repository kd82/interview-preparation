from collections import deque
from typing import Deque, List

def maxAreaOfIsland(grid: List[List[int]]) -> int:
        def bfs(grid, i, j):
            queue = deque()
            queue.append([i,j])
            count = 0
            while queue:
                curr = queue.popleft()
                for d in DIRS:
                    x = curr[0] + d[0]
                    y = curr[1] + d[1]
                    if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != 1:
                        continue
                    count += 1
                    grid[x][y] = -1
                    queue.append([x, y])
            return count
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1 or (i, j) in seen:
                return 0
            seen.add((i,j))
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j - 1) + dfs(i , j + 1)
        count = 0
        DIRS = [[-1,0],[1,0],[0, 1],[0, -1]]
        seen = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = max(bfs(grid, i, j), count, 1)
        return count
def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        def findArea(grid, i, j):
            grid[i][j] = 2
            area = 1
            if i + 1 < self.m and grid[i + 1][j] == 1:
                area += findArea(grid, i + 1, j)
            if j + 1 < self.n and grid[i][j + 1] == 1:
                area += findArea(grid, i, j + 1)
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                area += findArea(grid, i - 1, j)
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                area += findArea(grid, i, j - 1)
            return area
        maxArea = 0
        self.m, self.n = len(grid), len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                    if grid[i][j] == 1:
                        area = findArea(grid, i, j)
                        maxArea = max(area, maxArea)
        return maxArea
"""
1. Think recursively and make sure you follow only the viable path 
avoid keeping them in memory and only keep the valid ones
2. Very fast solutions are sometimes dfs when you wanna know max depth
"""