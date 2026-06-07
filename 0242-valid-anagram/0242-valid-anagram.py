class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        set_s = set(s)
        set_t = set(t)
        for i in set_s:
            dict_s[i] = s.count(i)
        for i in set_t:
            dict_t[i] = t.count(i)
        return dict_s == dict_t
        