class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        a = set([min(r) for r in matrix])
        b = set([max([r[c] for r in matrix]) for c in range(len(r))])

        return list(a.intersection(b))