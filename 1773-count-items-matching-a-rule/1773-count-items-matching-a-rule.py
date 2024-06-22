class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        return len([j for j in items if ruleValue == j[["type", "color", "name"].index(ruleKey)]])
