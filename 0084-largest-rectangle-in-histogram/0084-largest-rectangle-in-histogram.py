class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i,h in enumerate(heights):
            start_i = i
            while stack and stack[-1][1]>h:
                pop_i, pop_h = stack.pop()
                area = pop_h * (i - pop_i)
                max_area = max(area,max_area)
                start_i = pop_i
            stack.append((start_i, h))
        for i, h in stack:
            area = h * (len(heights)-i)
            max_area = max(area,max_area)
        return max_area 