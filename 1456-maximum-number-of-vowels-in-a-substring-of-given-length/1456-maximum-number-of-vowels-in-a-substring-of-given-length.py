class Solution(object):
    def maxVowels(self, s, k):
        best=0
        count=0
        for i,x in enumerate(s):
            if x in "aeiou":
                count+=1

            if i>=k and s[i-k] in "aeiou":
                count-=1

            best=max(best,count)

        return best    