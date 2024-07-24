class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        # Initialize the matrix correctly
        mat = [[0] * n for _ in range(m)]
        
        # Process the indices to increment rows and columns
        for r, c in indices:
            # Increment all elements in row `r`
            for j in range(n):
                mat[r][j] += 1
                
            # Increment all elements in column `c`
            for i in range(m):
                mat[i][c] += 1
        
        # Count the number of cells with odd values
        odd_count = 0
        for row in mat:
            for cell in row:
                if cell % 2 != 0:
                    odd_count += 1
        
        return odd_count