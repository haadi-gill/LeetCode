class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = []
        ncopy = n
        while(n>0):
            digits.append(int(n%10))
            n = int(n/10)
        
        sumDigits = sum(digits)
        prodDigits = 1
        for i in digits:
            prodDigits *= i
        
        return ncopy % (sumDigits + prodDigits) == 0