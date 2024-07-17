class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        

        count = 0

        while mainTank > 0:
            if mainTank < 5:
                count += mainTank
                mainTank = 0
            
            else:
                count += 5
                mainTank -= 5
                if additionalTank > 0:
                    mainTank += 1
                    additionalTank -= 1

    
        return count*10