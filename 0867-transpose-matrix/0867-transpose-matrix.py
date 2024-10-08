class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0])

        ans = []

        for j in range(m):
            temp = []
            for i in range(n):
                temp.append(matrix[i][j])
            ans.append(temp)

        return ans