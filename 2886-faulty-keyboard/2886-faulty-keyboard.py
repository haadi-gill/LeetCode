class Solution:
    def finalString(self, s: str) -> str:
        o = ""
        for c in s:
            if c == 'i':
                o = o[::-1]
            else:
                o += c

        return o