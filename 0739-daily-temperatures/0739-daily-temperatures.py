class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      n = len(temperatures)
      answer = [0] * n
      cur_max = temperatures[-1]      
      for i in range(n-1, -1, -1):
        t = temperatures[i]
        if t >= cur_max: cur_max = t
        else:
          i_nxt = i + 1
          while temperatures[i_nxt] <= t: i_nxt += answer[i_nxt]
          answer[i] = i_nxt - i
      return answer