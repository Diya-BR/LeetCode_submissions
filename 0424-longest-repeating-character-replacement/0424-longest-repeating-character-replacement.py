class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        ch_count = {}
        max_len = 0
        for right in range(len(s)):
            ch_count[s[right]] = ch_count.get(s[right],0) + 1
            max_freq = max(max_freq,ch_count[s[right]])
            while (right-left+1)-max_freq > k:
                ch_count[s[left]] -= 1
                left += 1
            max_len = max(max_len,(right-left+1))
        return max_len