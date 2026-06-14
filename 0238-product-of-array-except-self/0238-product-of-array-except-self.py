class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0
        res = [0]*len(nums)
        for num in nums:
            if num == 0:
                zeros += 1
                if zeros > 1:
                    return res
                continue
            prod *= num
        if zeros == 1:
            index = nums.index(0)
            res[index] = prod
            return res
        else:
            return [prod//num for num in nums]
         
