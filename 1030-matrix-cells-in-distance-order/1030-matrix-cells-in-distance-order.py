class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        # Step 1: Generate all coordinates in the matrix
        cells = [(r, c) for r in range(rows) for c in range(cols)]
        
        # Step 2: Sort by Manhattan distance from (rCenter, cCenter)
        cells.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        
        return cells