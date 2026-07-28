import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        count_t = collections.Counter(t)
        have, need = 0, len(count_t)
        window = {}
        res, res_len = [-1,-1], float("inf")
        left = 0
        for right in range(len(s)):
            char = s[right]
            if char in count_t:
                window[char] = window.get(char,0) + 1
                if window[char] == count_t[char]:
                    have += 1
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                left_char = s[left]
                if left_char in count_t:
                    window[left_char] -= 1
                    if window[left_char] < count_t[left_char]:
                        have -= 1
                left += 1
        l, r = res
        return s[l: r+1] if res_len != float('inf') else ""

        

