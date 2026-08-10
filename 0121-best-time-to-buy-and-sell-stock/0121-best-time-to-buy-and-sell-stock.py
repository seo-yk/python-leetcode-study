class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for cur in prices:
            min_price = min(min_price, cur)
            max_profit = max(max_profit, cur - min_price)

        return max_profit