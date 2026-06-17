class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]
        sum_max = 0
        sum_min = 0
        total = sum(nums)
        for num in nums:
            sum_max += num
            sum_min += num
            if max_sum<sum_max:
                max_sum = sum_max
            if sum_max < 0:
                sum_max = 0
            if min_sum>sum_min:
                min_sum = sum_min
            if sum_min>0:
                sum_min = 0
        if total == min_sum:
            return max_sum
        return max(max_sum, total-min_sum)
                
            