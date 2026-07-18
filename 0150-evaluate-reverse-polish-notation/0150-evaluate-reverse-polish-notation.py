class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i in ['+','-','*','/']:
                r = int(stack.pop())
                l = int(stack.pop())
                if i == '+':
                    stack.append(l+r)
                elif i == '-':
                    stack.append(l-r)
                elif i == '*':
                    stack.append(l*r)
                elif i == '/':
                    stack.append(l/r)
                continue
            stack.append(i)
        return int(stack[-1])