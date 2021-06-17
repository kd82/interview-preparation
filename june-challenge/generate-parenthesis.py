from collections import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(o, c, curr):
            if len(curr) == n * 2:
                res.append(str(curr))
                return
            if o < n:
                generate(o + 1, c, curr + "(")
            if c < o:
                generate(o, c + 1, curr + ")")
        res = []
        generate(0, 0, "")
        return res

"""
Key things to notice here
1. It is not optimal to generate all and check if they are valid
2. Notice the conditions as there are two ifs which is typical 
3. one to check we can add the open paranthesis and  if not do not add them in the else 
for example 
when backtracking there might be possible that we have more closed than required.
"""