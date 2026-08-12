class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = nums[0]
        max_prod = nums[0]
        res = nums[0] 
        for right in range(1,len(nums)):
            if nums[right]<0:
                min_prod, max_prod = max_prod, min_prod 
            max_prod = max(nums[right],max_prod*nums[right])
            min_prod = min(nums[right],min_prod*nums[right])
            res = max(res,max_prod)

        return res
           