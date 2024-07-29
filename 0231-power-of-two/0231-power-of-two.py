class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 1
        count = 1

        while (x <= n):
            if x == n:
                return True
            x = 2 ** count
            count += 1
        
        return False
