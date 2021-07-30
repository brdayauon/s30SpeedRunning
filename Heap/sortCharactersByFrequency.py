class Solution:
    def frequencySort(self, s: str) -> str:
        hm = {}
        for i in range(len(s)):
            c = s[i]
            if c not in hm:
                hm[c] = 1
            else:
                hm[c] += 1
                
        heap = []
        
        #key=Letter Values=Frequency
        for key,values in hm.items(): 
            #-values so that it's a maxheap
            heapq.heappush(heap, (-values, key))
        
        res = []
        while heap:
            freq, letters = heapq.heappop(heap)
            freq = freq* -1
            for i in range(freq):
                res.append(letters)
                
        return ''.join(res)