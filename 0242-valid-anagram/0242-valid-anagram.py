class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count_letters1 = {}
        count_letters2 = {}

        for i in range(len(s)):
            count_letters1[s[i]] = count_letters1.get(s[i],0)+1
            count_letters2[t[i]] = count_letters2.get(t[i],0)+1
        
        if count_letters1 == count_letters2:
            return True
        return False

        

