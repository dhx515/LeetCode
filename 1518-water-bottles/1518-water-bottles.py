class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        res = numBottles
        numEmpty = numBottles
        while numEmpty >= numExchange:
            new_bottles = numEmpty//numExchange
            res += new_bottles
            numEmpty = numEmpty % numExchange + new_bottles

        return res