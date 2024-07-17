from collections import deque

class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        
        d  = 0

        for l in logs:
            if l == "../":
                if d > 0:
                    d -= 1
            elif l == "./":
                continue
            else:
                d += 1

        return d