class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand = ["+", "-", "*", "/"]
        for i in range(len(tokens)):
            item = tokens[i]
            if item in operand:
                num2 = stack.pop()
                num1 = stack.pop()
                if item == "+":
                    res = num1+num2
                    stack.append(res)
                elif item == "/":                
                    res = num1/num2
                    stack.append((int)(res))
                elif item == "-":
                    res = num1-num2
                    stack.append(res)
                elif item == "*":
                    res  = num1 * num2
                    stack.append(res)
            else:
                stack.append(int(item))
        return stack[-1]