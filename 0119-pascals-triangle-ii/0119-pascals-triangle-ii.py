class Solution(object):
    def getRow(self, numRows):
        res = [1]
        if numRows == 0:
            return res

        res.insert(0, 0)
        res.append(0)

        for i in range(1, numRows + 1):
            temp = []
            for j in range(len(res) - 1):
                temp.append(res[j] + res[j + 1])
            temp.insert(0, 0)
            temp.append(0)
            res = temp

        return res[1: -1]