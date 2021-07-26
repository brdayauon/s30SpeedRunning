class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        holder = [0 for i in range(n)]
        for pair in trust:
            holder[pair[0]-1] -= 1
            holder[pair[1]-1] += 1     
        for i in range(len(holder)):
            if holder[i] == n-1:
                return i+1
        return -1