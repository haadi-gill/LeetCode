class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        xCoor = 0
        yCoor = 0
        count = 0

        xPos = 0
        yPos = 0

        while(board[xPos][yPos] != 'R'):
            yPos += 1
            xPos += yPos/8
            yPos %= 8

        xRef = xPos
        yRef = yPos
        
        xPos -= 1
        while(xPos > 0 and board[xPos][yPos] == '.'):
            xPos -= 1
        
        if board[xPos][yPos] == 'p':
            count += 1

        xPos = xRef + 1

        while(xPos < 7 and board[xPos][yPos] == '.'):
            xPos += 1
        
        if board[xPos][yPos] == 'p':
             count += 1

        xPos = xRef
        yPos -= 1


        while(yPos > 0 and board[xPos][yPos] == '.'):
             yPos -= 1
        
        if board[xPos][yPos] == 'p':
            count += 1

        yPos = yRef + 1

        while(yPos < 7 and board[xPos][yPos] == '.'):
            yPos += 1
        
        if board[xPos][yPos] == 'p':
            count += 1


        return count