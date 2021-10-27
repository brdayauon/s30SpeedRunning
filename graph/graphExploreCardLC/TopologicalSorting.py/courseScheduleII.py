#topological sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for i in range(numCourses)]
        hm = defaultdict(set)
        for prereq in prerequisites:
            hm[prereq[1]].add(prereq[0])
            indegree[prereq[0]] += 1
            
        stack = []
        res = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                stack.append(i)
                res.append(i)
        while stack:
            curr = stack.pop()
            
            if curr in hm:
                neighbors = hm[curr]
                for n in neighbors:
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        stack.append(n)
                        res.append(n)
        for i in range(len(indegree)):
            if indegree[i] != 0:
                return []
        return res
            