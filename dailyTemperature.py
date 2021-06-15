class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        monotonic stack solution
        """
        res = [0 for i in range(len(T))]
        
        if not T:
            return res
        stack = []
        
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        
        return res