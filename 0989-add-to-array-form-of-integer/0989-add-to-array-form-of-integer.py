class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        total = int(''.join(map(str, num))) + k
        return list(map(int, str(total)))