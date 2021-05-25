def toLowerCase1(s: str): # first version that I came up with 
        return s.lower()
def toLowerCase2(s: str): # By using ASCII
        res = []
        for i in range(len(s)):
            if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
                res.append(chr(ord(s[i]) - ord('A') + 97))
            else:
                res.append(s[i])
        return "".join(res)
def toLowerCase(s: str)-> str:
    is_upper = lambda x : 'A' <= x <= 'Z'
    to_lower = lambda x : chr(ord(x) | 32)
    return ''.join([to_lower(x) if is_upper(x) else x for x in s])
def main():
    print(toLowerCase('Hello'))
if __name__ == "__main__":
    main()
    """
    Key Takeaways:
    Can use lamda if the function is short and it is very elegant syntax 
    """