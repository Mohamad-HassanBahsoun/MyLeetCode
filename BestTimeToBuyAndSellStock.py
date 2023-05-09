class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        buy = prices[0]
        max = 0
        for i in range(1, len(prices)):
            if(buy > prices[i]):
                buy = prices[i]
            elif(prices[i]-buy > max):
                max = prices[i]-buy
        return max