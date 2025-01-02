class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        
        # Calculate the xy-plane projection
        xy_projection = sum(1 for row in grid for val in row if val > 0)
        
        # Calculate the yz-plane projection
        yz_projection = sum(max(row) for row in grid)
        
        # Calculate the zx-plane projection
        zx_projection = sum(max(col) for col in zip(*grid))
        
        # Total projection area
        return xy_projection + yz_projection + zx_projection