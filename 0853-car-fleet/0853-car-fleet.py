class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = sorted(zip(position,speed), reverse = True)
        stack = []
        for p,s in car:
            t = (target-p)/s
            if stack and stack[-1]>=t:
                continue
            stack.append(t)
        return len(stack)
        