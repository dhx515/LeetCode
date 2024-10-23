class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0
        
        curTime = timeSeries[0]
        poisonedTime = 0
        timer = duration
        
        for time in timeSeries[1:]:
            while curTime < time:
                if timer > 0:
                    poisonedTime += 1
                timer -= 1
                curTime += 1
            curTime = time
            timer = duration
            
        if timer:
            poisonedTime += timer
            
        return poisonedTime