#draw it out on the whiteboard to ensure understanding
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hm = defaultdict(set) # node: destination, weight
        
        for source, target, weight in times:
            hm[source].add((target,weight))
        seen = set()
        pq = []
        #cost and node
        heapq.heappush(pq,(0, k))
        
        while pq:
            cost, curr = heapq.heappop(pq)
            
            seen.add(curr)
            if len(seen) == n:
                return cost
            if curr in hm:
                neighbors = hm[curr]
                for destination, weight in neighbors:
                    if destination not in seen:
                        heapq.heappush(pq, (cost+weight, destination))
        return -1