from typing import List

class SegmentTree():
    def __init__(self, arr):
        n = len(arr)
        self.tree = [0]*(4*n)
        self.createTree(arr, 0, 0, n - 1)
        
    def merge(self, a, b):
        return a + b

    def createTree(self, arr: List[int], index: int, lo: int, hi: int):
        if lo == hi:  # base case
            self.tree[index] = arr[lo]
            return
        mid = (lo + hi)//2
        self.createTree(arr, 2 * index + 1, lo, mid) # go to the left
        self.createTree(arr, 2 * index + 2, mid + 1, hi) # go to the right
        self.tree[index] = self.merge(self.tree[2 * index + 1], self.tree[2 * index + 2])
        
    def querySegTree(self, index: int, i: int, j: int, lo: int, hi: int):
        if lo > j or hi < i: # completely outside range
            return 0
        if i <= lo and j >= hi:
            return self.tree[index]
        mid = (lo + hi)//2
        if i > mid:
            return self.querySegTree(2*index + 2, i, j, mid + 1, hi)
        elif j <= mid:
            return self.querySegTree(2*index + 1, i, j, lo, mid)
        leftQuery = self.querySegTree(2*index + 1, i, mid, lo, mid)
        rightQuery = self.querySegTree(2*index + 2, mid + 1, j, mid + 1, hi)
        return self.merge(leftQuery, rightQuery)
    
    def updateValue(self, index, i, val, lo, hi):
        if lo == hi:
            self.tree[index] = val
        mid = (lo + hi)//2
        if i > mid:
            return self.querySegTree(2*index + 2, i, val, mid + 1, hi)
        elif i <= mid:
            return self.querySegTree(2*index + 1, i, val, lo, mid)
        self.tree[index] = self.merge(self.tree[2 * index + 1], self.tree[2 * index + 2])
        
def main():
    arr = [1,3,5]
    tree = SegmentTree(arr)
    print(tree.tree)
    print(tree.querySegTree(0, 0, 2, 0, len(arr) - 1))
    tree.updateValue(0, 1, 2, 0, len(arr) - 1)
    print(tree.querySegTree(0, 0, 2, 0, len(arr) - 1))
if __name__ == "__main__":
    main()
