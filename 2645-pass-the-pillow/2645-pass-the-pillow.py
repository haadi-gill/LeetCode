class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        if (time/(n-1))%2==0:
            return 1 + (time%(n-1))
        else:
            return n - (time%(n-1))