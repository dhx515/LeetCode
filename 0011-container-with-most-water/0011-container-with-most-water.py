class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        leftPointer, rightPointer = 0, len(height)-1
        while rightPointer-leftPointer > 0:
            res = max(res, (rightPointer-leftPointer)*min(height[leftPointer], height[rightPointer]))
            
            if height[leftPointer] > height[rightPointer]:
                rightPointer -= 1
            else:
                leftPointer += 1
        return res