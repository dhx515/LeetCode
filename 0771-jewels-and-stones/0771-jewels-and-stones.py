class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        mem = {}
        for jewel in jewels:
            mem[jewel] = 0
        
        stones = list(stones)
        ans = 0
        for stone in stones:
            if stone in mem:
                ans += 1
        
        return ans