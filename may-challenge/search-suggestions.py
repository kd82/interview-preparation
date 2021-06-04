from typing import DefaultDict, List
import bisect
def suggestProductsWithBisect(products, searchWord):
    products.sort()
    res, prefix, i = [], '', 0
    for c in searchWord:
        prefix += c
        i = bisect.bisect_left(products, prefix, i)
        res.append([w for w in products[i: i + 3] if w.startswith(prefix)])
    return res
def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        res = []
        for i in range(len(searchWord)):
            res.append(trie.search(searchWord[:i+1]))
        return res
class TrieNode:
    def __init__(self):
        self.children = DefaultDict(TrieNode)
        self.isWord = False
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.isWord = True
    def search(self, word):
        self.res = []
        curr = self.root
        for c in word:
            if c not in curr.children:
                return []
            curr = curr.children[c]
        def dfs(curr, w):
            if len(self.res) == 3:
                return
            if curr.isWord:
                self.res.append(word + w)
            for key in sorted(curr.children):
                dfs(curr.children[key], w + key)
        dfs(curr, '')
        return self.res
def main():
    print(suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"]
, "mouse"))

if __name__ == "__main__":
    main()

"""
Key Takeaways:
1. Learn how to implement Trie in Python 
2. Implement Trie on your own next Time 
3. Use Default Dict to simplify Code and reduced if else statements
4. Keep the code clean
"""