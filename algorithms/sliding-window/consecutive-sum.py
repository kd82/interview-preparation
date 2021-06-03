"""
Given an array of integers of size ‘n’.
Our aim is to calculate the maximum sum of ‘k’ 
consecutive elements in the array.

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4 
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23}
of size 4.

Input  : arr[] = {2, 3}
         k = 3
Output : Invalid
There is no subarray of size 3 as size of whole
array is 2.
"""
from typing import List
def findMaximumConsecutiveSum(arr: List[int], k: int) : # Brute Force Method
    maxSum, n = 0, len(arr) 
    for i in range(n - k + 1):
       maxSum = max(maxSum, sum(arr[i: i + k]))
    return maxSum

def slidingWindow(arr, k):
    n = len(arr)
    if n < k:
        return -1
    curr = sum(arr[:k])
    maxSum = curr
    for j in range(n - k):
        curr = curr - arr[j] + arr[j + k]
        maxSum = max(curr, maxSum)
    return maxSum

def main():
    print(findMaximumConsecutiveSum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
    print(slidingWindow([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
if __name__ == '__main__':
    main()