class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        numDrank = 0
        numFull = numBottles
        numEmpty = 0
            
        while(numFull > 0 or numEmpty > numExchange):
            numDrank += numFull
            numEmpty += numFull
            numFull = int(numEmpty / numExchange)
            numEmpty -= numFull * numExchange

        return numDrank

        return numDrank