
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        dict_n = collections.Counter(nums)
        n = 0
        dict_n =  dict(sorted(dict_n.items(), key=lambda item: item[1], reverse=True))
        for key in dict_n:
            res.append(key)
            n += 1
            if n == k:
                break
        return res
