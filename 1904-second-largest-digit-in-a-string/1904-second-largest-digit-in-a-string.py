from collections import defaultdict

class Solution:
    def secondHighest(self, s: str) -> int:
        d = defaultdict(int)

        d = {k:(d[k]+1) for k in sorted([c for c in s if c.isdigit()])}

        if len(d.keys()) < 2:
            return -1


        return int( list(d.keys())[-2]) 
        