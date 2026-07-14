class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [str.lower() for str in s if str.isalnum()]
        return s[::-1] == s