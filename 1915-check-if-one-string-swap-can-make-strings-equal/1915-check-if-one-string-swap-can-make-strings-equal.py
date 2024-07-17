class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1 = str(s1)
        s2 = str(s2)
        diffIndex = -1
       # if [c for c in s1].sort() != [c for c in s2].sort(): return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if diffIndex == -1:
                    diffIndex = i
                else:
                    s1 =  s1[:diffIndex] + s1[i] + s1[diffIndex+1:i] + s1[diffIndex] + s1[i+1:]
                    break
        return s1 == s2  