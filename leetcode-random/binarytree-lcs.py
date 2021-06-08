from collections import deque


class TreeNode:
    def __init__(self) -> None:
        self.left, self.right = None, None
        self.val = 0

def longestConsecutive1(root: TreeNode) -> int: # 
        def dfs(root, parent, length):
            if not root: return
            length = length + 1 if parent and root.val == parent.val + 1 else 1
            #max_len = max(max_len, length)
            dfs(root.left, root, length)
            dfs(root.right, root, length)
        max_len = 0
        dfs(root, None, 0)
        return max_len
def longestConsecutive2(root: TreeNode) -> int: # 
        def dfs(root, parent, length):
            if not root: return length
            length = length + 1 if parent and root.val == parent.val + 1 else 1
            return max(length, dfs(root.left, root, length), dfs(root.right, root, length))
        return dfs(root, None, 0)
def longestConsecutive3(root: TreeNode):
    if not root:
        return 0
    stack = deque()
    stack.append([root, 1])
    max_len = 1
    while stack:
        curr, length = stack.pop()
        if curr.left:
            stack.append([curr.left, length + 1 if curr.val + 1 == curr.left.val else 1])
        if curr.right:
            stack.append([curr.right, length + 1 if curr.val + 1 == curr.right.val else 1])
        max_len = max(max_len, length)
    return max_len

def main():
    print(longestConsecutive3())