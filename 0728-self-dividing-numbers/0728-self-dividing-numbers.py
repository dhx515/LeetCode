class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for target in range(left, right+1):
            stringTarget = str(target)
            
            flag = True
            for charTarget in stringTarget:
                curTarget = int(charTarget)
                if curTarget == 0 or target % curTarget != 0:
                    flag = False
            
            if flag:
                ans.append(target)
        
        return ans