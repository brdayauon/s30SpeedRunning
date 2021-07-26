#BFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #indegree array/basically visited
        indegree = [0 for i in range(len(rooms))]
        hm = {}
        #make adjacency matrix as well as update indegree array
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if i not in hm:
                    hm[i] = set()
                hm[i].add(rooms[i][j])
                indegree[rooms[i][j]] += 1

        #queue/stack
        queue = deque([0])
        visited = set()
        while queue:
            curr = queue.popleft()
            if curr not in visited and curr in hm:
                #check neighbors
                neighbors = hm[curr]
                for n in neighbors:
                    indegree[n] = 0 #mark as entered key
                    if indegree[n] == 0:
                        queue.append(n)
            #add to visited so we don't visit this node again
            visited.add(curr)
        
        #once we finished everything the indegree array will have all 0 but one room if there is an invalid room
        for i in range(len(indegree)):
            if indegree[i] != 0:
                return False
        return True
        
#DFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #indegree array/basically visited
        indegree = [0 for i in range(len(rooms))]
        hm = {}
        #make adjacency matrix as well as update indegree array
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if i not in hm:
                    hm[i] = set()
                hm[i].add(rooms[i][j])
                indegree[rooms[i][j]] += 1

        #queue/stack
        stack = [0]
    
        visited = set()
        while stack:
            curr = stack.pop()
            if curr not in visited and curr in hm:
                #check neighbors
                neighbors = hm[curr]
                for n in neighbors:
                    indegree[n] = 0 #mark as entered key
                    if indegree[n] == 0:
                        stack.append(n)
            #add to visited so we don't visit this node again
            visited.add(curr)
        
        #once we finished everything the indegree array will have all 0 but one room if there is an invalid room
        for i in range(len(indegree)):
            if indegree[i] != 0:
                return False
        return True
        