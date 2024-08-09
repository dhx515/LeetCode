class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        minDist = float('inf')
        ans = -1
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                manDist = abs(points[i][0]-x)+abs(points[i][1]-y)
                if manDist<minDist:
                    ans = i
                    minDist = manDist
        return ans