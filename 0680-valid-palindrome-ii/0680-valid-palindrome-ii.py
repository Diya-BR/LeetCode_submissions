class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        left = 0
        right = len(s) -1
        removed = 0
        def helper(left: int,right: int) -> list:
            while left<right :
                if s[left] != s[right]:
                    return [False,left,right]
                left += 1
                right -= 1 
            return [True,0,0]
        res = helper(left,right)

        if not res[0] :
            left = res[1]
            right = res[2]
            r1 = helper(left+1,right)
            r2 = helper(left,right-1)
            return r1[0] or r2[0]
        else:
            return True
        