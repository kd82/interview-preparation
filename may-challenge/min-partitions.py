def minpartitions(self, n):
    return int(max(n))
"""
One of the possible explanations for this is
1. Let's say we have a number 3024 
We need minimum numbers to make the target as zeros and ones are allowed so 
we have to add 1s to get the digits independently which looks like 
3024
1  1  
1 11
0 11
1  1
When we add this up we should get the target
"""