"""
Create a trie node class:
    - each node is going to have a property of children {} and boolean isEnd.

In class Trie:
    - make a pointer to the head of the TrieNode():
When inserting:
    - we create a pointer to the head.
    - iterate through the word.
        - at each char .. create a TrieNode() if char does not exist amongst the children..
        move current pointer (curr = curr.children[c])
    - at the end set the isEnd boolean at the current TrieNode to True

When searching: 
    - we create a pointer to the head.
    - iterate through the word.
        - for each character.. if it is not amongst the children.. then return False
        else move current pointer to the children.
    - if the isEnd boolean property is true.. return True
    - return False otherwise
When startWith:
    - we create pointer to the head
    - we iterate through the word
        - if character not among children.. return False 
        - else move to children.
    at the end return True

"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.head 
        for i in range(len(word)):
            c = word[i]
            if c not in curr.children:
                curr.children[c] = TrieNode() #createTrieNode not {}
            curr = curr.children[c]
        curr.isEnd = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.head 
        for i in range(len(word)):
            c = word[i]
            if c in curr.children:
                curr = curr.children[c] #forget else statement
            else:
                return False
        if curr.isEnd == True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.head 
        for i in range(len(prefix)):
            c = prefix[i]
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True
                
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


#DO AGAIN WARMUP