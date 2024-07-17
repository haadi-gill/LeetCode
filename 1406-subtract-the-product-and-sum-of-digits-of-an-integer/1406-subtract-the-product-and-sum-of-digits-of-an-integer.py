class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        productN = 1
        sumN = 0
        while n > 0:
            productN *= n%10
            sumN += n%10
            n /= 10
        
        return productN - sumN