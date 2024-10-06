class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visit=set()
        n=len(grid)
        m=len(grid[0])
        ans = 0
        def dfs(i,j):
            if i>=n or j>=m or i<0 or j<0 or grid[i][j]==0:
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            ans=dfs(i,j+1)
            ans+=dfs(i+1,j)
            ans+=dfs(i,j-1)
            ans+=dfs(i-1,j)
            return ans
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    return dfs(i,j)