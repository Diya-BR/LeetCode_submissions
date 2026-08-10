class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findfirst(nums: List[int],target: int) -> int:
            left = 0
            right = len(nums)-1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    idx = mid
                    right = mid - 1
                elif nums[mid] < target: 
                    left = mid + 1
                else:
                    right = mid - 1
                print(idx)
            return idx
        def findlast(nums: List[int],target: int) -> int:
                left = 0
                right = len(nums)-1
                idx = -1
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] == target:
                        idx = mid
                        left =  mid + 1
                    elif nums[mid] < target: 
                        left = mid + 1
                    else:
                        right = mid - 1
                return idx
        return [findfirst(nums,target),findlast(nums,target)]




        