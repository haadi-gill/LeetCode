class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = [int(x) for x in bin(n)[2:]]

        max_count = 0
        curr_count = 1
        start_count = False

        for i in b:
            if i :
                if not start_count:
                    start_count = True
                else:
                    if curr_count > max_count:
                        max_count = curr_count
                    curr_count = 1
            elif start_count:
                curr_count += 1
                
        return max_count
        