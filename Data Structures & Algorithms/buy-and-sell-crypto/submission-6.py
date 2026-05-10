class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre_min: int = prices[0]
        res = 0

        for i in range(1, len(prices)):
            if pre_min > prices[i]:
                pre_min = prices[i]
            else:
                res = max(res, prices[i] - pre_min)
        
        return res
