class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        prev = curr = 0
        target_len = n1 + n2
        i = j = 0
        med = target_len//2
        for _ in range(med+1):
            prev = curr
            if i < n1 and (j>=n2 or nums1[i]<nums2[j]):
                curr = nums1[i]
                i+=1
            else:
                curr = nums2[j]
                j+=1
        if target_len%2 == 0:
            return (prev+curr)/2
        return curr