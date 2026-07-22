from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False    
        s1_count = Counter(s1)
        s2_len = len(s2)
        left = 0
        count_check = {}
        for right in range(len(s2)):
            char = s2[right]
            if char in s1_count:
                if char not in count_check:
                    count_check[char] = 0
                count_check[char] += 1
                while count_check[char] > s1_count[char]:
                    left_char = s2[left]
                    if left_char in count_check:
                        count_check[left_char] -= 1
                        if count_check[left_char] == 0:
                            del count_check[left_char]
                    left += 1
                if count_check == s1_count:
                    return True
            else:
                count_check.clear()
                left = right + 1
            
        return False

            
            
                        