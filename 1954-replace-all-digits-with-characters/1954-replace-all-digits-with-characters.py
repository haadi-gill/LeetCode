class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        shifted = ''

        for i in range(len(s)):
            if i % 2 == 1:
                shifted += chr(ord(s[i-1]) + int(s[i]))
            else:
                shifted += s[i]
        
        return shifted