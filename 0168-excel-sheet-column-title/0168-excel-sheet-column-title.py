class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""
        while columnNumber > 0:
            index = (columnNumber - 1) % 26
            result = chr(index + ord('A')) + result
            columnNumber = (columnNumber - 1) // 26
        return result