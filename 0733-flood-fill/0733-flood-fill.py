class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        originColor = image[sr][sc]
        
        rowSize, colSize = len(image), len(image[0])
        
        visit = [[0 for _ in range(colSize)] for _ in range(rowSize)]
        visit[sr][sc] = 1
        
        queue = [[sr, sc]]
        
        while queue:
            cr, cc = queue.pop()
            image[cr][cc] = color
            
            for dr, dc in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                nr, nc = cr + dr, cc + dc
                if not (0 <= nr < rowSize and 0 <= nc < colSize):
                    continue
                if image[nr][nc] != originColor:
                    continue
                if visit[nr][nc] == 1:
                    continue
                    
                queue.append([nr,nc])
                visit[nr][nc] = 1
        
        return image