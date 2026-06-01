class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sub = 0
        min_buy = prices[0]

        for sell in prices:
            max_sub = max(max_sub, sell - min_buy)
            min_buy = min(min_buy, sell)
        
        return max_sub