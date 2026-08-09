class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        max_count = 0
        for i,j in count.items():
            if j>len(nums)//2:
                return i