class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        today_temp = temperatures[0]
        stack = []
        res = [0]*len(temperatures)
        for i in range(0,len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                poped = stack.pop()
                res[poped] = i - poped
            stack.append(i)
        return res



