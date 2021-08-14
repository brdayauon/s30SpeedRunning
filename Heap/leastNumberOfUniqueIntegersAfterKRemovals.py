class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hm = {}
        for i in range(len(arr)):
            if arr[i] not in hm:
                hm[arr[i]] = 1
            else:
                hm[arr[i]] += 1
        heap = []
        for key,v in hm.items():
            heapq.heappush(heap, (v, key))
        while k and heap:
            frequency, number = heapq.heappop(heap)
            for i in range(frequency):
                if k == 0:
                    break
                hm[number] -= 1
                if hm[number] == 0:
                    del hm[number]
                k -= 1
            if k == 0:
                break
        return len(hm)