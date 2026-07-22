class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2
        l, r  = 0, m
        while l <= r:
            i = (l + r) // 2
            j = half_len - i
            l1 = (i == 0) and float("-inf") or nums1[i-1]
            r1 = (i == m) and float("inf") or nums1[i]
            l2 = (j == 0) and float("-inf") or nums2[j-1]
            r2 = (j == n) and float("inf") or nums2[j]
            if l1 <= r2 and l2 <= r1:
                if (n+m) % 2 == 0:
                    return (max(l2,l1) + min(r1,r2))/2.0
                else:
                    return max(l1,l2)
            elif l1 > r2:
                r = i - 1
            else:
                l = i + 1
        return 0
