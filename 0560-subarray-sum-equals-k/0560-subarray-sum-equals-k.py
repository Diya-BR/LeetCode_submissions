class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        dict_track = {0:1}
        for num in nums:
            curr_sum += num
            if curr_sum - k in dict_track:
                count += dict_track[curr_sum - k]
            dict_track[curr_sum] = dict_track.get(curr_sum,0)+1
        return count
