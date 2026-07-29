class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        curr = 0
        while curr not in visited:
            visited.add(curr)
            curr = nums[curr]
        return curr