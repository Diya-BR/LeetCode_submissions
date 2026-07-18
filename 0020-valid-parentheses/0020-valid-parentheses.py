class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para = {')':'(', ']':'[','}':'{'}
        for i in s:
            if i in para.keys():
                if not stack or stack[-1] != para[i]:
                        return False
                stack.pop()
            else:
                stack.append(i)
        
        return len(stack) == 0
