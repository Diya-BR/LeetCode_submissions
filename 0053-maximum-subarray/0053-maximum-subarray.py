class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum>max_sum:
                max_sum = sum
            if sum < 0:
                sum = 0
        return max_sum