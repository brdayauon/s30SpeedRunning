class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        count = 0
        for i in range(len(word)):
            count += 1
            if ch == word[i]:
                break
        return self.reverse(word, 0, count-1)
    def reverse(self, word, left, right):
        word = list(word)
        while left < right:
            temp = word[left]
            word[left] = word[right]
            word[right] = temp
            left += 1
            right -= 1 
        return ''.join(word)