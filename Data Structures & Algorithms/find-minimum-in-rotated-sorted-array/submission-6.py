class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float("inf")

        while l <= r:
            mid = (r - l) // 2 + l
            res = min(res, nums[mid])

            if nums[l] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        
        return res