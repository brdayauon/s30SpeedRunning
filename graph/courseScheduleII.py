class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #create adjacency list
        indegree = [0 for i in range(numCourses)]
        hm = {}
        
        for edge in prerequisites:
            if edge[1] not in hm:
                hm[edge[1]] = []
            hm[edge[1]].append(edge[0])
            indegree[edge[0]]+= 1
            
        stack = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                stack.append(i)
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr)
            if curr in hm:
                neighbors = hm[curr]
                for n in neighbors:
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        stack.append(n)
                        
        for i in range(len(indegree)):
            if indegree[i] != 0:
                return []
            
        return res

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hm = {}
        
        for prereq in prerequisites:
            if prereq[1] not in hm:
                hm[prereq[1]] = []
            hm[prereq[1]].append(prereq[0])
            
        indegree = [0] * numCourses
        queue = deque([])

        for i in range(len(prerequisites)):
            indegree[prerequisites[i][0]] += 1
            
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            if curr in hm:
                neighbors = hm[curr]
                if neighbors:
                    for n in neighbors:
                        indegree[n] -= 1
                        if indegree[n] == 0:
                            queue.append(n)
        
        for i in range(len(indegree)):
            if indegree[i] != 0:
                return []
                        
        return res