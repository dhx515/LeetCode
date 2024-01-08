class Solution(object):
    def replaceElements(self, arr):
        n = len(arr)-1
        great = arr[-1]
        
        arr[n] = -1
        
        for i in range(n-1, -1, -1):
            cur = arr[i]
            arr[i] = great
            if great < cur:
                great = cur
                
        return arr