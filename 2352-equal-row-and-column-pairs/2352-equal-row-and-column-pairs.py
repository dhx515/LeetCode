class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = []
        cols = []
        
        n = len(grid)
        for i in range(n):
            rows.append(' '.join(map(str, grid[i])))
            
            tmp = [grid[j][i] for j in range(n)]
            cols.append(' '.join(map(str, tmp)))
            
        ans = 0
        for i in range(n):
            for j in range(n):
                if rows[i] == cols[j]:
                    ans += 1
        
        return ans