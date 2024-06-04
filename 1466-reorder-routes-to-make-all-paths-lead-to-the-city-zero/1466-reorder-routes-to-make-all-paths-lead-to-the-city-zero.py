class Solution(object):
    def __init__(self):
        ans = 0

    def minReorder(self, n, nums):
        out = {} # city a to b
        dest = {} # which city connected w b
        for i , j in nums:
            out[i] = out.get(i , []) + [j]
            dest[j] = dest.get(j , []) + [i]
        
        visit = [0]*n
        self.ans = 0
        self.dfs(dest, out, 0, visit, 0)
        return self.ans
        
    def dfs(self, d, out, index, visit, p):
        if visit[index]:
            return
        visit[index] = 1
        if index in d:
            for i in d[index]:
                self.dfs(d , out , i , visit , index)
        if index in out:
            for j in out[index]:
                if j != p:
                    self.ans += 1
                self.dfs(d , out , j , visit , index)