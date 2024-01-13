class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        mem = {}
        for iter in range(len(magazine)):
            cur = magazine[iter]
            if cur not in mem.keys():
                mem[cur] = 1
            else:
                mem[cur] += 1
        
        res = True  
        for iter in range(len(ransomNote)):
            cur = ransomNote[iter]
            if cur not in mem.keys() or mem[cur] -1 < 0:
                res = False
                break
            mem[cur] -= 1
            
        return res
        