class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = [ord(c) for c in s]
        return sum([abs(m[i] - m[i+1]) for i in range(len(s)-1)])