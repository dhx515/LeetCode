class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        ROWS = len(text1) + 1
        COLS = len(text2) + 1
        dp = [[0] * COLS for _ in range(ROWS)]

        for i in range(1, ROWS):
            for j in range(1, COLS):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[ROWS-1][COLS-1]