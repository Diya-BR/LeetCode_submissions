class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_l = 0
        max_r = 0
        total_w = 0
        while(l<r):
            max_l = max(height[l],max_l)
            max_r = max(height[r],max_r)
            if max_l<max_r:
                total_w += max_l - height[l]
                l += 1
            else:
                total_w += max_r - height[r]
                r -= 1
        return total_w