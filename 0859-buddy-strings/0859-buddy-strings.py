class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        if A == B and len(A) != len(set(A)):
            return True
        
        diffs = []
        for i in range(len(A)):
            if A[i] != B[i]:
                diffs.append(i)
                if len(diffs) > 2:
                    return False
                
        return len(diffs) == 2 and A[diffs[0]] == B[diffs[1]] and A[diffs[1]] == B[diffs[0]]