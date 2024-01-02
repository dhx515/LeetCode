class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        
        tmp = ''.join(map(str, nums))
        tmpList = list(map(str, tmp.split('0')))
        return len(str(max(tmpList)))