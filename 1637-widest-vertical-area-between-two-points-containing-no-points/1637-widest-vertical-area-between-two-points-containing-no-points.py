class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        arr=[]
        for i in range(len(points)):
            arr.append(points[i][0])
        arr.sort()
        
        ans=0
        for i in range(len(arr)-1):
            ans=max(ans,(arr[i+1]-arr[i]))
        
        return ans