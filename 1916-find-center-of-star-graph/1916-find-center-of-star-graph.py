class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        o = defaultdict(int)
        n = len(edges)

        for a in edges:
            o[a[0]] += 1
            if o[a[0]] == n:
                return a[0]
            o[a[1]] += 1
            if o[a[1]] == n:
                return a[1]
            