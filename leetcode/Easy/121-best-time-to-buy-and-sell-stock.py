class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_prices = [0] * n
        max_prices[-1] = prices[-1]
        for i in range(n-2, -1, -1):
            max_prices[i] = max(max_prices[i+1], prices[i])
        
        return max([max_prices[i] - prices[i] for i in range(n)])