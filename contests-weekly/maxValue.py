def maxValue(n: str, x: int) -> str:
      # isNegative = True if n[0] == '-' else False
      # if isNegative:
      #     i = 1
      #     while i < len(n):
      #         if int(n[i]) > x:
      #             break
      #         i += 1
      # else:
      #     i = 0
      #     while i < len(n):
      #         if int(n[i]) < x:
      #             break
      #         i += 1
      # return n[:i]+str(x)+n[i:]
      isNegative = False
      if n[0] == '-':
            isNegative = True
            n = n[1:]
      for i in range(len(n)):
            num = int(n[i])
            if not isNegative and num < x or isNegative and num > x:
                return n[:i]+str(x)+n[i:] if not isNegative else "-"+n[:i]+str(x)+n[i:]
      return n+str(x) if not isNegative else "-"+n + str(x)
"""
1. Code can be simpler.
2. Show off your coding skills 
Avoid Repeating the Code
"""
