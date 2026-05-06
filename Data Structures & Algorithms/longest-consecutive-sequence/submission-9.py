class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_ele = set(nums)
        res = 0

        for n in nums:
            if n - 1 in set_ele:
                continue
            curr = n
            while curr + 1 in set_ele:
                curr += 1
            
            res = max(res, curr - n + 1)
    
        return res
                    