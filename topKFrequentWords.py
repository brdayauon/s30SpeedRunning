#TC O(NlogK)
#SC O(N)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or k == 0:
            return []
        
        #find frequency of each word (put into hm)
        hm = {}
        for word in words:
            if word not in hm:
                hm[word] = 1
            else:
                hm[word] += 1
        heap = []
        
        #for word in hm put it into heap based on frequency
        for word,freq in hm.items():
            heapq.heappush(heap, (-freq, word))
        
        res = []
        while k > 0:
            freq, word = heapq.heappop(heap)
            res.append(word)
            k -= 1
        return res