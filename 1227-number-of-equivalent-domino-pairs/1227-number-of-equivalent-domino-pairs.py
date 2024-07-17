import math
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        
        defdict = defaultdict(int)

        for d in dominoes:
            s = sorted(d)
            defdict[(s[0], s[1])] += 1
        return sum([math.comb(s,2) for s in defdict.values()])