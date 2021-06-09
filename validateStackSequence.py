class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        TC: O(m+n)
        SC: O(N)
        """
        stack = []
        j = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            
            while stack and j < len(popped)-1 and popped[j] == stack[-1]:
                stack.pop()
                j += 1
            
            if len(stack) != 0 and popped[j] == stack[-1]:
                stack.pop()
                
        return not stack