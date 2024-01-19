class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        
        minimum_val = float("inf")
        for iter in range(len(arr)-1):
            minimum_val = min(minimum_val, arr[iter+1] - arr[iter])
        
        res = []
        for iter in range(len(arr)-1):
            if arr[iter+1] - arr[iter] == minimum_val:
                res.append([arr[iter], arr[iter+1]])
        
        return res