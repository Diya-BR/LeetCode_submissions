class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        
        
        peak_idx = 0
        max_val = height[0]
        for i in range(n):
            if height[i] > max_val:
                max_val = height[i]
                peak_idx = i
                
        water = 0
        
        
        left_max = 0
        for i in range(peak_idx):
            left_max = max(left_max, height[i])
            water += left_max - height[i]
            
        right_max = 0
        for i in range(n - 1, peak_idx, -1):
            right_max = max(right_max, height[i])
            water += right_max - height[i]
            
        return water