class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.count = 0
        self.wholeWordCount = 0
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root 
        for i in range(len(word)):
            c = word[i]
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.count += 1
        curr.isEnd = True
        curr.wholeWordCount += 1

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.root 
        for i in range(len(word)):
            c = word[i]
            if c not in curr.children:
                return 0
            else:
                curr = curr.children[c]
        return curr.wholeWordCount 
    

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.count 

    def erase(self, word: str) -> None:
        curr = self.root 
        for i in range(len(word)):
            c = word[i]
            if c not in curr.children:
                return 0
            curr = curr.children[c]
            curr.count -= 1
        curr.wholeWordCount -= 1 

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)