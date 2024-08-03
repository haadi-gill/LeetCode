class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float('infinity')
        maxProfit = 0

        for p in prices:
            if p < minPrice:
                minPrice = p
            
            profit = p - minPrice

            if profit > maxProfit:
                maxProfit = profit

        return maxProfit