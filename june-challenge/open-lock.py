from collections import List
from collections import Deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        queue = Deque(["0000"])
        visited = set(deadends)
        visited.add("0000")
        depth = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr == target:
                    return depth
                for i in range(4):
                    x = int(curr[i])
                    for d in (-1, 1):
                        y = (x + d) % 10
                        next = curr[:i] + str(y) + curr[i + 1:]
                        if next not in visited:
                            queue.append(next)
                            visited.add(next)
                            
            depth += 1
        return -1
"""
1. Use the template when using bfs 
2. Learned a new way to go back and front when using the numbers 
instead of writing regular if else code 
3. instead of using two seperate sets one for deadends and one for visited 
we could have used only one 
4. Visited is needed because of the fact that we might go back to the original state
and we don't want to do that.
"""