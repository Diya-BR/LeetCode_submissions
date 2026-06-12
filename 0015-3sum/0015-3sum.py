class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            # Skip duplicate 'i'
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            n1 = i + 1
            n2 = len(nums) - 1
            
            while n1 < n2:
                current_sum = nums[i] + nums[n1] + nums[n2]
                
                if current_sum == 0:
                    # Append directly; no need to sort or check "not in res"
                    res.append([nums[i], nums[n1], nums[n2]])
                    
                    # Skip duplicate n1 and n2 values by stepping by 1
                    while n1 < n2 and nums[n1] == nums[n1 + 1]:
                        n1 += 1
                    while n1 < n2 and nums[n2] == nums[n2 - 1]:
                        n2 -= 1
                        
                    # Move past the final duplicates
                    n1 += 1
                    n2 -= 1
                    
                elif current_sum < 0:
                    n1 += 1
                else:
                    n2 -= 1
                    
        return res