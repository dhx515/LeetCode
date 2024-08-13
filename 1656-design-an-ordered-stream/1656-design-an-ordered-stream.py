class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.pointer = 1
        self.elist = [None] * (n+1)
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.elist[idKey] = value
        result = []
        while self.pointer < len(self.elist) and self.elist[self.pointer]:
            result.append(self.elist[self.pointer])
            self.pointer += 1
        return result
    
    
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)