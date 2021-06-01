def hasPathWithGivenSum(t, s):
    if not t:
        return False
    s -= t.value
    if not t.left and not t.right:
        return s == 0
    return hasPathWithGivenSum(t.left, s) or hasPathWithGivenSum(t.right, s)
"""
Key Take Aways:
1. See how the values are changed in the recursive call stack
"""