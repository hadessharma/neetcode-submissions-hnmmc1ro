class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res: list[int] = [] 
        def dfs(i: int, rem: int, sub: list) -> None:
            if rem < 0 or i >= len(nums):
                return
            
            if rem == 0:
                res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i, rem - nums[i], sub)
            # dfs(i + 1, rem - nums[i], sub)

            sub.pop()
            dfs(i + 1, rem, sub)
            return
        
        # return res
        dfs(0, target, [])
        return res
