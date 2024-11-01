class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        caseAll = True
        caseNot = True
        caseFirst = True
        
        for i, c in enumerate(word):
            if ord(c) not in range(ord('A'), ord('Z')+1):
                caseAll = False
                if i == 0:
                    caseFirst = False
            if ord(c) not in range(ord('a'), ord('z')+1):
                caseNot = False
                if i != 0:
                    caseFirst = False
        
        return caseAll or caseNot or caseFirst