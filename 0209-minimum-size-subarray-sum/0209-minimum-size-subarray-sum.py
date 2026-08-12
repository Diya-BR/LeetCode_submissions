class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        max_sum = 0
        win_size = float("inf")
        for right in range(len(nums)):
            max_sum += nums[right]
            while max_sum >= target:
                win_size = min(right - left +  1,win_size)
                max_sum -= nums[left]
                left += 1
          
        return win_size if win_size != float("inf") else 0
        


            