class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        n -= 1
        if (time/(n))%2==0:
            return 1 + (time%(n))
        else:
            return n - (time%(n))