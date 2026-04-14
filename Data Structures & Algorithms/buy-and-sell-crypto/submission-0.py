class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use 2 pointer method

        n = len(prices)
        i, j = 0, 1
        res = 0

        while j < n:
            if prices[i] < prices[j]:
                sell = prices[j]
                buy = prices[i]

                profit = sell - buy 
                res = max(res, profit)
            else:
                i = j
            j += 1



       
        

        return res 
        