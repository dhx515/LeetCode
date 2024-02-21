class Solution(object):
    def trap(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        res, l , r, lMax, rMax = 0, 0, len(h) - 1, 0, 0
        
        if r < 2: return res

        while l < r:
            if h[l] < h[r]:
                lMax = max(lMax, h[l])
                res += lMax - h[l]
                l += 1
            else:
                rMax = max(rMax, h[r])
                res += rMax - h[r]
                r -= 1
        
        return res