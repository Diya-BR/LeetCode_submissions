class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > len(nums):
            k = k - len(nums)
        nums_saved = nums[len(nums)-k:] 
        
        i = len(nums)-k
        for i in range(len(nums)-1,k-1,-1):
            nums[i] = nums[i-k]
        
        for i in range(k):
            nums[i] = nums_saved[i]
        return