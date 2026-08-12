class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        unique = []
        max_count = 0
        count = 0
        for right in range(len(s)):
            
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
                count -= 1
                
            unique.append(s[right])
            count += 1
            max_count = max(count,max_count)
        return max_count 


            