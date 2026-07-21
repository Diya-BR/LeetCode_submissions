class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            sum = 0
            for i in piles:
                sum += (i + mid - 1) // mid

            if sum > h:
                left = mid + 1
            else:
                right = mid 
        return right