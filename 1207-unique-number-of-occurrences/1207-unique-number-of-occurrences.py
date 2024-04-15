class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        return len(set(Counter(arr).values()))==len(Counter(arr).values())