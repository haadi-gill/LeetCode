class Solution:
    def checkDivisibility(self, n: int) -> bool:
        ncopy = n
        sumDigits = 0
        prodDigits = 1

        while(ncopy>0):
            sumDigits += ncopy%10
            prodDigits *= ncopy%10 
            ncopy //= 10
        
        return n % (sumDigits + prodDigits) == 0