from collections import List
from collections import Deque

def minimumSemesters1(n: int, relations: List[List[int]]) -> int:
        indegree = [0]*(n + 1)
        graph = [[] for _ in range(n + 1)]
        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1
        queue = Deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                queue.append(i)
        courses, steps = 0, 0
        while queue:
            size = len(queue)
            steps += 1
            for _ in range(size):
                curr = queue.popleft()
                courses +=1 
                for nei in graph[curr]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
        return steps if courses == n else -1
def minimumSemesters2(n: int, relations: List[List[int]]) -> int: #Approach 2
        visited = {}
        graph = {i: [] for i in range(1, n + 1)}
        for src, dest in relations:
            graph[src].append(dest)
        def dfs(node):
            if node in visited:
                return visited[node]
            visited[node] = -1
            for i in range(len(graph[node])):
                if dfs(graph[node][i]):
                    return True
            visited[node] = False
            return False
        for node in graph:
            if dfs(node):
                return -1
        visited_length = {}
        def dfs_max_depth(node):
            if node in visited_length:
                return visited_length[node]
            max_length = 1
            for end_node in graph[node]:
                length = dfs_max_depth(end_node)
                max_length = max(max_length, length + 1)
            visited_length[node] = max_length
            return max_length
        return max(dfs_max_depth(node) for node in graph)
def minimumSemesters3(n: int, relations: List[List[int]]) -> int:
        visited = {}
        graph = {i: [] for i in range(1, n + 1)}
        for src, dest in relations:
            graph[src].append(dest)
        visited = {}
        def dfs_max_depth(node):
            if node in visited:
                return visited[node]
            visited[node] = -1
            max_length = 1
            for end_node in graph[node]:
                length = dfs_max_depth(end_node)
                if length == -1:
                    return -1
                max_length = max(max_length, length + 1)
            visited[node] = max_length
            return max_length
        max_length = -1
        for node in graph.keys():
            length = dfs_max_depth(node)
            if length == -1:
                return -1
            max_length = max(length, max_length)
        return max_length