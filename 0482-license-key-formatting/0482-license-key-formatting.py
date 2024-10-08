class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace("-","")
        
        if len(s) <= k : 
            return s.upper()
        
        if len(s)%k == 0 :
            return "-".join(s[i:i+k].upper() for i in range(0,len(s),k))
        else :
            return s[:len(s)%k].upper() + "-" + "-".join(s[i:i+k].upper() for i in range(len(s)%k,len(s),k)) 