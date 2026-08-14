class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_dict = collections.Counter(nums)
        for i,n in count_dict.items():
            if n<2:
                return i