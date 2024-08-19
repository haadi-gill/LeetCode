class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        c = Counter(commands)
        r = (c.get("RIGHT", 0))
        l = (c.get("LEFT",0))
        d = (c.get("DOWN",0))
        u = (c.get("UP",0))
        return n*(d-u)+(r-l)