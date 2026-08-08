class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2 and n == 0:
            return
        i = 0
        j = 0
        k = 0
        num_dummy = nums1[:m]
        while i<m and j<n:
            if num_dummy[i] < nums2[j]:
                nums1[k] = num_dummy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        while i<m:
            nums1[k] = num_dummy[i]
            i += 1
            k+=1
        while j<n:
            nums1[k] = nums2[j]
            j += 1
            k += 1
        return 
        

            


        