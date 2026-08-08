class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        prev = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != prev:
                prev = nums[l] = nums[i]
                l += 1
        return l
                