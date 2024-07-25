arr = []

def heapify(n, i):
    global arr
    
    m = i
    l, r = 2*m+1 ,2*m+2

    if l < n and arr[m] < arr[l]:
        m = l
    
    if r < n and arr[m] < arr[r]:
        m = r

    if m != i:
        temp = arr[m]
        arr[m] = arr[i]
        arr[i] = temp
        heapify(n, m)

    
    
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        global arr
        arr = nums
        n = len(nums)
            
        if n == 1:
            return nums
        elif n == 2:
            if nums[0] < nums[1]:
                return nums
            else:
                return nums[::-1]
        for a in range(n, -1, -1):
            heapify(n,a)

        for b in range(n-1, 0, -1):
            temp = arr[b] 
            
            arr[b] = arr[0]
            arr[0] = temp
            heapify(b, 0)

        return(arr)
