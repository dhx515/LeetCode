class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split(" ")
        s = [ele for ele in s if ele.strip()]
        return len(s)