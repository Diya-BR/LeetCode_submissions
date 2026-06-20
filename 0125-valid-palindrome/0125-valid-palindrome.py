class Solution:
    def isPalindrome(self, s: str) -> bool:
        list = []
        
        s= s.lower().strip()
        for char in s:
            if char== " " or char ==",":
                continue
            if char.lower().isalnum():
                list.append(char)
        print(list)
        for i in range(len(list)//2):
            if list[i] != list[len(list)-i-1]:
                return False
        return True


