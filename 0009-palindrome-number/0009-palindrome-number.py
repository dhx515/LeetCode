class Solution(object):
    def isPalindrome(self, x):
        xPrime = str(x)
        res = True
        for iter in range(len(xPrime)//2):
            if xPrime[iter] != xPrime[len(xPrime)-1-iter]:
                res = False
                break
        return res