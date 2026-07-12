class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        Can do this by tracking lowest previous price.
        and tracking most profit made so far

        """

        profit = 0
        buy_price = prices[0]
        n = len(prices)

        for i in range(1, n):

            sell_price = prices[i]
            current_profit = sell_price - buy_price

            if current_profit > profit:
                profit = current_profit

            if sell_price < buy_price:
                buy_price = sell_price


        return profit
        