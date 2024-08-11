class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        filtered = [min(rectangle) for rectangle in rectangles]
        
        maxSide = max(filtered)
        
        ans = filtered.count(maxSide)
        return ans