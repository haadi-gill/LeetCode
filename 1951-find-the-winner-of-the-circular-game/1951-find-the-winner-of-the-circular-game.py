class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        l = range(1, n+1)
        index = 1
        
        while(len(l) > 1):
            index = (index+k-1)%len(l)
            l.pop(index-1)
            if index == 0: index = 1
            
        
        return l[0]