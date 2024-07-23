class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        
        l, r = 1, x/2

        while l < r:
            i = (l + r) // 2
            b = i ** 2
            # print("left "+ str(l) + " right " + str(r) + " i " + str(i) +  " b " + str(b))
            if b == x:
                # print('equal')
                return i
            elif b > x:
                # print('greater')
                r = i-1
            else:
                # print('less')
                l = i + 1
        
        i = (l + r) // 2
        b = i ** 2
        # print("left "+ str(l) + " right " + str(r) + " i " + str(i) +  " b " + str(b))
        return i if b <= x else i - 1