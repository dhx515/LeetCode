class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        c = n // 2
        ans = 0
        for i in range(n):
            ans += mat[i][i]
            ans += mat[n-1-i][i]
        if n % 2 == 1:
            ans -= mat[c][c]
        return ans