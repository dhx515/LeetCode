class Solution(object):
    def duplicateZeros(self, arr):
        res = list()
        for iter in arr:
            if iter == 0:
                res.append(iter)
            res.append(iter)
            
            if len(res) >= len(arr):
                break
                
        for i in range(len(arr)):
            arr[i] = res[i]