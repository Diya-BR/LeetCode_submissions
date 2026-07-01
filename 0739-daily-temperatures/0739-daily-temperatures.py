class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        curr = temperatures[-1]
        for i in range(n-1,-1,-1):
            t = temperatures[i]
            if t >= curr: curr = t
            else:
                next_i = i + 1
                while temperatures[next_i]<=t: next_i += ans[next_i]
                ans[i] = next_i - i
        return ans