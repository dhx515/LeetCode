class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def triangle_area(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return abs(x1*1.0 * (y2*1.0 - y3*1.0) + x2*1.0 * (y3*1.0 - y1*1.0) + x3*1.0 * (y1*1.0 - y2*1.0)) / 2

        max_area = 0
        for p1, p2, p3 in combinations(points, 3):
            max_area = max(max_area, triangle_area(p1, p2, p3))
        
        return max_area