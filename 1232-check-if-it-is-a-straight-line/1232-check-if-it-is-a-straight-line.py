class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        # 모든 x 좌표가 같다면 수직선
        if all(x == x1 for x, y in coordinates):
            return True
        
        # 기준 기울기 계산 (x2-x1이 0이 아니라고 가정)
        dx, dy = x2 - x1, y2 - y1
        
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            # 기울기 비교: (y - y1) / (x - x1) == dy / dx
            if (y - y1) * dx != (x - x1) * dy:
                return False
        
        return True