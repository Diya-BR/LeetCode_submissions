class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_count = 0
        dict_present = {}
        for right in range(len(s)):
            dict_present[s[right]] = dict_present.get(s[right],0) + 1
            while (right - left + 1) - max(dict_present.values()) > k:
                dict_present[s[left]] -= 1
                left += 1
            max_count = max(max_count,right - left + 1)
        return max_count
