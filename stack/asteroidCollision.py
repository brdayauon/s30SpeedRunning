class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
            else:
                #if negative or same sign
                if stack[-1] < 0 or ((stack[-1] < 0 and asteroids[i] < 0)  or (stack[-1]>0 and asteroids[i] > 0)):
                    stack.append(asteroids[i])
                    continue
                #current asteroid is negative and top of stack is positive
                while stack and (stack[-1] > 0 and asteroids[i] < 0):
                    
                    if abs(asteroids[i]) == abs(stack[-1]):
                        stack.pop()
                        break
                    elif abs(asteroids[i]) > abs(stack[-1]):
                        stack.pop()
                        if not stack or stack[-1] < 0:
                            stack.append(asteroids[i])
                    elif abs(asteroids[i]) < abs(stack[-1]):
                        break
                
        return stack