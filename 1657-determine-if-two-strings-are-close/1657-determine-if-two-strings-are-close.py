class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        mem1 = Counter(word1)
        mem2 = Counter(word2)
        cnt1 = []
        cnt2 = []
        
        if len(word1)!=len(word2) and len(mem1)!=len(mem2):
            return False
        
        for c in mem2:
            if c in mem1 and mem1[c] == mem2[c]:
                pass
            elif c in mem1:
                cnt1.append(mem1[c])
                cnt2.append(mem2[c])
            else:
                return False
        
        if len(cnt1)!=len(cnt2):
            return False
        
        cnt1.sort()
        cnt2.sort()
        if cnt1 != cnt2:
            return False
        
        return True