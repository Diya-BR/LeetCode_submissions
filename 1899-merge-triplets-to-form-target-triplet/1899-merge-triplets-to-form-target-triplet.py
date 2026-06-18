class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = set()
        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue
            if t[0] == target[0]: res.add(0)
            if t[1] == target[1]: res.add(1)
            if t[2] == target[2]: res.add(2)
            if len(res) == 3:
                return True
        return False
