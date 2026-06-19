import collections
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique = sorted(set(nums))
        max_streak = 1
        cur_streak = 1
        for i in range(1,len(unique)):
            if unique[i] == unique[i-1]+1:
                cur_streak += 1
            else:
                    max_streak=max(max_streak,cur_streak)
                    cur_streak = 1
        return max(max_streak,cur_streak)