def maxProduct(words):
    def calculateHash(word):
        hash = 0
        for c in word:
            hash |= 1 << (ord(c) - 97)
        return hash
    n = len(words)
    values = [0]*len(words)
    for i in range(n):
        values[i] = calculateHash(words[i])
    maxLen = 0
    for i in range(n):
        for j in range(n):
            if (values[i] & values[j]) == 0:
                maxLen = max(maxLen, len(words[i])*len(words[j]))          
    return maxLen
def main():
    words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    print(maxProduct(words))
    
if __name__ == "__main__":
    main()
    
"""
Key Takeaways:
1. Use Bits to your advantage and use them like a map
"""