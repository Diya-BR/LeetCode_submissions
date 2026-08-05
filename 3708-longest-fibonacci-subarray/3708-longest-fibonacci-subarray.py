class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 2
        curr = 2
        a, b = nums[0], nums[1]
        for num in nums[2:]:
            if num == a + b:
                curr += 1
                res = max(res, curr)
            else:
                curr = 2
            a, b = b, num
        return res
            