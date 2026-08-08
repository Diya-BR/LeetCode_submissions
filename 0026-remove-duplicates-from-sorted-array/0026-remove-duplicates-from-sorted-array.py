class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []
        k = 0
        for i in range(len(nums)):
            if nums[i] not in seen :
                nums[k] = nums[i]
                seen.append(nums[i])
                k+=1
        return k
                