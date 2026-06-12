class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_map = Counter(a+b for a in nums1 for b in nums2)
        total_tuples = 0
        for c in nums3:
            for d in nums4:
                complement = -(c+d)
                if complement in sum_map:
                    total_tuples += sum_map[complement]
        return total_tuples

        