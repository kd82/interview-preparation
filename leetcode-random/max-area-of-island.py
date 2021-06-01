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
        count = 0
        DIRS = [[-1,0],[1,0],[0, 1],[0, -1]]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = max(bfs(grid, i, j), count, 1)
        return count