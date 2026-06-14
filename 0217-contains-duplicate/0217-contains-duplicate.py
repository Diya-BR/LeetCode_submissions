class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_lis_numset = list(set(nums))
        return len(set_lis_numset) != len(nums)

        