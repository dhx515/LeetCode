class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = [[0]*i for i in range(1,numRows+1)]
        
        for i in range(numRows):
            output[i][0] = 1
            for j in range(1, i):
                output[i][j] = output[i-1][j] + output[i-1][j-1]
            output[i][i] = 1
        return output