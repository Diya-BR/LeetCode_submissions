class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        max_len = 2
        max_i = 2
        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] == nums[i+2]:
                max_i += 1
                max_len = max(max_i, max_len)
            else:
                max_i = 2
        return max_len



        