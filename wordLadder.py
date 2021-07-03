from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        seen = set()
        for i in range(len(wordList)):
            seen.add(wordList[i])
        
        seen.add(beginWord)
        count = 1
        queue = deque([beginWord])
        letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        while queue:
            size = len(queue)
            count += 1
            for i in range(size):
                word = queue.popleft()
                word = list(word)
                #change each letter of the word
                for i in range(len(word)):
                    prev = word[i]
                    for j in range(len(letters)):
                        word[i] = letters[j]
                        if prev == letters[j]:
                            continue
                        if ''.join(word) == endWord:
                            return count
                        elif ''.join(word) in seen:
                            queue.append(''.join(word))
                            seen.remove(''.join(word))
                    word[i] = prev       
        return 0