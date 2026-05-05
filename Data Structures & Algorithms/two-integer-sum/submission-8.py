class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp: dict[int, int] = {}

        for i, n in enumerate(nums):
            if target - n in mp:
                return [mp[target - n], i]
            mp[n] = i
        return [-1, -1]
