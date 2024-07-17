class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        sum = 0
        lastStop = 0

        #print("Current Sum:", sum, "Last Stop:", lastStop)

        for c in customers:
            arrival = c[0]
            duration = c[1]
            
            if arrival < lastStop:
                waitTime = lastStop + duration - arrival
            else:
                waitTime = duration
                
            lastStop = arrival + waitTime
            sum += waitTime
            #print("Arrived at:", arrival, ", waited ", waitTime, "until", lastStop)
            
        return float(sum)/len(customers)