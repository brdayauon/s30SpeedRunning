class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hm = defaultdict(set)
        
        for edge in edges:
            hm[edge[0]].add(edge[1])
            hm[edge[1]].add(edge[0])
        
        stack = []
        seen = set()
        count = 0
        for i in range(n):
            if i not in seen:
                seen.add(i)
                stack.append(i)
                count += 1
                
                while stack:
                    curr = stack.pop()
                    neighbors = hm[curr]
                    for n in neighbors:
                        if n not in seen:
                            seen.add(n)
                            stack.append(n)
        return count
                        
        
        
        
# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         hm = defaultdict(set)
        
#         for edge in edges:
#             hm[edge[0]].add(edge[1])
#             hm[edge[1]].add(edge[0])
        
#         queue = deque([])
#         seen = set()
#         count = 0
#         for i in range(n):
#             if i not in seen:
#                 seen.add(i)
#                 queue.append(i)
#                 count += 1
                
#                 while queue:
#                     curr = queue.popleft()
#                     neighbors = hm[curr]
#                     for n in neighbors:
#                         if n not in seen:
#                             seen.add(n)
#                             queue.append(n)
#         return count
                        
        
        
        
