class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            for i in range(0,len(s)):
                s_set = list(set(s))
                t_set = list(set(t))
                #t_dict = {}
                t_dict = {}
                for i in t_set:
                    t_dict[i]=t.count(i)
                for i in s_set:
                    if s.count(i) != t_dict.get(i, 0):
                        return False
                return True  


                

        else:
            return False