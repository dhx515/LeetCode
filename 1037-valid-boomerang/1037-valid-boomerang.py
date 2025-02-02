class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False
        
        # 외적 계산
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]

        return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)