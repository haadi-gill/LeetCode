class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        s = sorted(heights)
        return len([h for i,h in enumerate(heights) if h != s[i]])