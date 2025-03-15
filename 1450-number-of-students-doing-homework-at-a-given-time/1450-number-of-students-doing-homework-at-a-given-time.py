class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        ans = 0
        
        loopLength = len(startTime)
        for i in range(loopLength):
            if queryTime in range(startTime[i], endTime[i]+1):
                ans += 1
        return ans