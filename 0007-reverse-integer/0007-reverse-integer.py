class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        
        if x<0:
            flag = True
        rev = 0
        x_copy = abs(x)
        while x_copy:
            rev = (x_copy % 10) + (10 * rev)
            x_copy = x_copy//10
       
        if flag:
            rev= -1 * rev
        if rev < -(2**31) or rev > (2**31) - 1:
            return 0
        return rev


        