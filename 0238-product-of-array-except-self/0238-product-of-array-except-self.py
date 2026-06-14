class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*n
        suc = [1]*n
        res = [1]*n
        for i in range(1,n):
            pre[i] = nums[i-1]*pre[i-1]
        for i in range(n-2,-1,-1):
            suc[i] = nums[i+1]*suc[i+1]
        for i in range(0,n):
            res[i] = pre[i]*suc[i]
        return res

