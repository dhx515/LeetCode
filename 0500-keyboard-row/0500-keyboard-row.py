class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        
        ans = []
        for word in words:
            cur = set(word.lower())
            for row in rows:
                if cur & row == cur:
                    ans.append(word)
                    break
        return ans