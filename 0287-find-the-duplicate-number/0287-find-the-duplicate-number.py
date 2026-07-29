class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(f"s: {slow}, f: {fast}")
            if fast == slow:
                break
        print(f"After")
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            print(f"s: {slow}, f: {fast}")
        return fast