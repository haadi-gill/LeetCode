class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if (high-low == 1):
            return 1
        elif (low%2==1) or (high%2==1):
            return (high-low)/2+1
        else:
            return (high-low)/2