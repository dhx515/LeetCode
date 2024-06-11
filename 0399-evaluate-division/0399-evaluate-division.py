class Solution(object):
    def __init__(self):
        seen = set()
        graph = defaultdict(dict)
    
    
    def calcEquation(self, equations, values, queries):
        self.graph = defaultdict(dict)
        
        for i in range(len(equations)):
            a, b = equations[i][0], equations[i][1]
            self.graph[a][b] = values[i]
            self.graph[b][a] = 1 / values[i]
        
        res = []
        for a, b in queries:
            if a not in self.graph or b not in self.graph:
                res.append(-1.0)
            else:
                self.seen = set()
                res.append(self.dfs(a,b,1))
        
        return res
    
    
    def dfs(self, start, end, res):
            if start in self.seen:
                return -1.0
            
            if start == end:
                return res
            self.seen.add(start)
            
            for n in self.graph[start]:
                if n not in self.seen:
                    tmp = self.dfs(n, end, res*self.graph[start][n]) 
                    #if tmp is -1, that means this path cannot find answer, not return
                    if tmp != -1.0:
                        return tmp
            
            return -1.0