class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        a = sorted(salary)[1:-1]
        return float(sum(a))/float(len(a))