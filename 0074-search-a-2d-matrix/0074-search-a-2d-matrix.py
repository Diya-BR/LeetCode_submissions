class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m * n) - 1
        while l <= r:
            mid = (l + r)//2
            i = mid // n
            j = mid % n
            val = matrix[i][j]
            if val == target:
                return True
            elif val < target:
                l = mid + 1
                
            else:
                r = mid - 1
                
        return False