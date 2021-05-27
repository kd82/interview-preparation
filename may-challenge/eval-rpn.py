from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in "*/+-":
                stack.append(int(c))
            else:
                l, r = stack.pop(), stack.pop()
                if c == '*':
                    stack.append(r*l)
                elif c == '+':
                    stack.append(r+l)
                elif c == '-':
                    stack.append(r-l)
                else:
                    stack.append(int(float(r)/l))
        return sum(stack)
"""
Take aways:
Python treats integer division differently 
We can use String comparison to make the code cleaner
"""