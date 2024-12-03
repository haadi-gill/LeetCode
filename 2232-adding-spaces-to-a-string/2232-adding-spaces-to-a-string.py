class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        print(len(s))
        print(len(spaces))
        if len(spaces) == len(s):
            return " " + (" ").join([c for c in s])


        for i in spaces[::-1]:
            s = s[:i] + " " + s[i:]
    
        return s