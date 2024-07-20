class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return not ('a' in s[s.find('b'):] and 'b' in s)