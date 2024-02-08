class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        ns = re.sub('[^0-9a-zA-Z]+', '', s)
        ns = ns.lower()
        
        mid = len(ns)//2
        left, right = 0, len(ns)-1
        
        for left in range(mid):
            if ns[left] != ns[right]:
                return False
            else:
                right -= 1
        return True