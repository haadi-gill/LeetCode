class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        s = set()
        v = []

        for a in arr:
            if a in s:
                try:
                    v.remove(a)
                except:
                    pass
                continue
            s.add(a)
            v.append(a)
    
        
            
        if len(v) < k:
            return ""
        else:
            return v[k-1]