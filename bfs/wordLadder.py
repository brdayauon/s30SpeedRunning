class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        seen = set(wordList)
        queue = deque([beginWord])
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        count = 0
        while queue:
            size = len(queue)
            count += 1
            for i in range(size):
                word = queue.popleft()
                word = list(word)
                #change every letter in word
                for letter in range(len(word)):
                    original = word[letter]
                    for alpha in range(len(alphabets)):
                        #change letter
                        if original == alphabets[alpha]:
                            continue
                        word[letter] = alphabets[alpha]
                        newWord = ''.join(word)
                        if newWord in seen:
                            if newWord == endWord:
                                return count+1
                            queue.append(newWord)
                            seen.remove(newWord)
                    word[letter] = original
        return 0