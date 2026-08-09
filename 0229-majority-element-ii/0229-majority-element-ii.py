class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        nums_arr = []
        n = len(nums)
        for i,j in count.items():
            if j>n//3:
                nums_arr.append(i)
        return nums_arr

