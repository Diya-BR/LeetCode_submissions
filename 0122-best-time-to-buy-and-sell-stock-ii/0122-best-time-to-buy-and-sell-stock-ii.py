class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        max_price = 0
        for i in range(len(prices)-1) :
            min_price = min(min_price, prices[i])
            if prices[i]>prices[i+1]:
                profit += prices[i] - min_price
                min_price = prices[i+1]
            elif i+1 == len(prices)-1:
                profit += prices[i+1] - min_price
            print(f"{min_price} {profit}")
        return profit


