class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paran = {'(':')','[':']','{':'}'}
        for char in s:
            if char in paran.keys():
                stack.append(paran[char])
            else:
                if not stack:
                    return False
                if stack[-1] == char:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
