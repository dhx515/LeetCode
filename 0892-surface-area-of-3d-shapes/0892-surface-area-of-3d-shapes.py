class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        total_area = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    # Add top and bottom faces
                    total_area += 2
                    
                    # Add side faces, accounting for overlaps
                    total_area += grid[i][j]
                    total_area -= min(grid[i][j], grid[i-1][j]) if i > 0 else 0
                    total_area += grid[i][j]
                    total_area -= min(grid[i][j], grid[i+1][j]) if i < n - 1 else 0
                    total_area += grid[i][j]
                    total_area -= min(grid[i][j], grid[i][j-1]) if j > 0 else 0
                    total_area += grid[i][j]
                    total_area -= min(grid[i][j], grid[i][j+1]) if j < n - 1 else 0
        
        return total_area