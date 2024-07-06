class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        newImage = [self.invert(row[::-1]) for row in image]
        return newImage
    
    def invert(self, targetList):
        newList = []
        for target in targetList:
            invertedTarget = 1 if target == 0 else 0
            newList.append(invertedTarget)
        return newList