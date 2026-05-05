class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen: set[int] = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        
        return False