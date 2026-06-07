class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<1 else 1
        x = abs(x)
        rev = 0
        while x:
            rev = (x % 10) + (rev * 10)
            x = x // 10
        rev = sign * rev
        if rev < (-2**31) or rev>(2**31-1):
            return 0
        return rev