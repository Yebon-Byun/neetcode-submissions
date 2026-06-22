class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        Example 1:

        Input: prices = [10,1,5,6,7,1]

        Output: 6
        Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.
        """

        # Brute Force
        res = 0 
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                res = max(res, sell - buy)

        return res
