class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        cnt = 0
        def dfs(i):
            isConnected[i][i] = 0
            for j in range(n):
                if isConnected[i][j] and isConnected[j][j]:
                    dfs(j)
                
        for i in range(n):
            if isConnected[i][i]:
                cnt += 1
                dfs(i)
        return cnt