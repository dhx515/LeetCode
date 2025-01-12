class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        return sum(1 for col in zip(*strs) if list(col) != sorted(col))
