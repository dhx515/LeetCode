class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        sorted_potions = sorted(potions)
        result = []
        for a in spells:
            count = len(sorted_potions) - bisect_left(sorted_potions, (success + a - 1) // a)
            result.append(count)
        return result