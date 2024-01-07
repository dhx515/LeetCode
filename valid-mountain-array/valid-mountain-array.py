class Solution(object):
    def validMountainArray(self, arr):
        temp = False
        valid = False
        n = len(arr)
        i = 0

        while i + 1 < n and arr[i] < arr[i+1]:
            i += 1
            valid = True
            
        while i + 1 < n and arr[i] > arr[i+1] and valid == True:
            i += 1
            temp = True
        
        if i+1 != n :
            temp = False
        
        return temp