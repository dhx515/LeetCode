class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        
        q = []
        fresh_count = 0
        
        # Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # If there are no fresh oranges initially
        if fresh_count == 0:
            return 0
        
        # Directions for 4 possible movements (up, down, left, right)
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        minutes = 0
        
        while q:
            next_q = []
            for r, c in q:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        # Mark the fresh orange as rotten
                        grid[nr][nc] = 2
                        # Decrease the fresh count since it's been rotten now
                        fresh_count -= 1
                        # Add the newly rotten orange to the queue for the next round
                        next_q.append([nr, nc])
            
            q = next_q
            if next_q:
                minutes += 1
        
        # If there are remaining fresh oranges, return -1 (impossible case)
        if fresh_count > 0:
            return -1
        else:
            return minutes
