class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        hm = defaultdict(set)
        for i in range(len(pid)):
            hm[ppid[i]].add(pid[i])
        res = []
        res.append(kill)
        
        stack = [kill]
        
        while stack:
            curr = stack.pop()
            
            neighbors = hm[curr]
            for i in ((neighbors)):
                res.append(i)
                stack.append(i)
        return res