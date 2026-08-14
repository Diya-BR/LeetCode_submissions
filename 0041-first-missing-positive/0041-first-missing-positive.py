class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr = [False for i in range(len(nums)+1)]
        for i in nums:
            if i>0 and i<=len(nums):
                arr[i-1] = True
                
        for i in range(len(nums)+1):
            if not arr[i]:
                return i+1