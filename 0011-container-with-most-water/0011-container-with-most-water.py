class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            Area = min(height[l],height[r])*(r-l)
            if Area > max_area:
                max_area = Area
            if  height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area 
        