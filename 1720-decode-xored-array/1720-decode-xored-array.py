class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        l=[first]
        for i in encoded:
            l.append(i^l[-1])
        return l  