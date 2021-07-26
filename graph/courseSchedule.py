# Time Complexity : O(Vertices + edges) where vertices is numCourses
# Space Complexity : O(vertices + edges) where vertices is numCourses
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #make adjacency list
        indegree = [0] * numCourses
        hm = {}
        
        #creating indegrees but putting subjects into indegree array. as well as put into hm 
        for edge in prerequisites:
            indegree[edge[0]] += 1
            if edge[1] not in hm:
                hm[edge[1]] = []
            hm[edge[1]].append(edge[0])
                
        queue = deque([])
        #check for independent nodes
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                
        #process queue
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr in hm:
                    edges = hm[curr]
                    if edges:
                        for edge in edges:
                            indegree[edge] -= 1
                            if indegree[edge] == 0:
                                queue.append(edge)
                                
        for i in range(len(indegree)):
            if indegree[i] != 0:
                return False
            
        return True
#DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
                
        while stack:
            curr = stack.pop()
            if curr in hm:
                neighbors = hm[curr]
                for n in neighbors:
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        stack.append(n)
                        
        for i in range(len(indegree)):
            if indegree[i] != 0:
                return False
            
        return True