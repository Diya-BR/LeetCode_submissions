class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_sum = -1<<32
        min_sum = 1<<32
        this_max = 0
        this_min = 0
        total = 0
        for n in nums:
            if this_min>0:
                this_min = 0
            if this_max<0:
                this_max = 0
            this_min += n
            this_max += n
            total +=n
            max_sum = max(max_sum, this_max)
            min_sum = min(min_sum, this_min)
        if max_sum<0:
            return max_sum
        return max(max_sum,total-min_sum)

        