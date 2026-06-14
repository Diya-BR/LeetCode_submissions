class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        farthest = nums[0]
        cur_jump = 0
        jumps_taken = 0
        for i,num in enumerate(nums):
            farthest = max(farthest,i+num)
            if i== cur_jump:
                jumps_taken += 1
                cur_jump = farthest
            if cur_jump >= len(nums)-1:
                    return jumps_taken
                
                
            
            

        