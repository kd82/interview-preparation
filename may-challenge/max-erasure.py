from typing import List
def maximumUniqueSubarray(nums: List[int]) -> int:
    n = len(nums)
    uniqueSet = set()
    i, j = 0, 0
    total, ans = 0, 0
    while i < n and j < n:
        if nums[j] not in uniqueSet:
            total += nums[j]
            ans = max(ans, total)
            uniqueSet.add(nums[j])
            j += 1
        else:
            total -= nums[i]
            uniqueSet.remove(nums[i])
            i += 1
    return ans
def main():
    print(maximumUniqueSubarray([4, 2, 4, 5, 6]))
if __name__ == "__main__":
    main()

"""
Practice more of the problems involving two pointers
every one of them are different
"""