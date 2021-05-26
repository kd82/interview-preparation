from typing import List

class SegmentTree:
    def __init__(self, arr):
        n = len(arr)
        self.tree = [0]*(4*n)
        self.buildTree(0, arr, 0, n - 1)

    def buildTree(self,index, arr, lo, hi):
        if lo == hi:
            self.tree[index] = arr[lo]
            return
        mid = (lo + hi)//2
        self.buildTree(2*index + 1, arr, lo, mid)
        self.buildTree(2*index + 2, arr, mid + 1, hi)
        self.tree[index] = self.tree[2*index + 1] + self.tree[2*index + 2]

    def update(self,treeIndex, index, val, lo, hi):
        if lo == hi:
            self.tree[treeIndex] = val
            return
        mid = (lo + hi)//2
        if index > mid:
            self.update(2*treeIndex + 2, index, val, mid + 1, hi)
        elif index <= mid:
            self.update(2*treeIndex + 1, index, val, lo, mid)
        self.tree[treeIndex] = self.tree[2*treeIndex + 1] + self.tree[2*treeIndex + 2]

    def query(self, treeIndex, i, j, lo, hi):
        if j < lo or i > hi:
            return 0
        if i <= lo and j >= hi:
            return self.tree[treeIndex]
        mid = (lo + hi)//2
        if i > mid:
            return self.query(2*treeIndex + 2, i, j, mid + 1, hi)
        elif j <= mid:
            return self.query(2*treeIndex + 1, i, j, lo, mid)
        left = self.query(2*treeIndex + 2, mid + 1, j, mid + 1, hi)
        right = self.query(2*treeIndex + 1, i , mid , lo, mid)
        return left + right
 
def main():
    arr = [1,2,5]
    tree = SegmentTree(arr)
    print(tree.tree)
    print(tree.query(0, 0, 2, 0, len(arr) - 1))
    tree.update(0, 1, 2, 0, len(arr) - 1)
    print(tree.tree)
    print(tree.query(0, 1, 2, 0, len(arr) - 1))
if __name__ == "__main__":
    main()