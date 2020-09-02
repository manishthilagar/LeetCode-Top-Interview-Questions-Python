class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #print(prices)
        dif = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                #print(prices[i])
                dif += prices[i] - prices[i-1]
        return dif
