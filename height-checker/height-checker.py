class Solution(object):
    def heightChecker(self, heights):
        new_heights = heights[:]
        new_heights.sort()
        res = 0
        for iter in range (len(heights)):
            if new_heights[iter] != heights[iter]:
                res += 1
        return res