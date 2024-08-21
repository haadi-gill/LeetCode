class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        pos = s.find('6')

        if pos == -1:
            return num
        return int(s[:pos] + '9' + s[pos+1:])