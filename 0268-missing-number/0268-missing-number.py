class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [False for i in range(len(nums)+1)]
        for i in nums:
            arr[i] = True
        for i in range(len(nums)+1):
            if not arr[i]:
                return i

        
