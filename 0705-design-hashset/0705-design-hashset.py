class MyHashSet(object):

    def __init__(self):
        self.keys = set()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.keys.add(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.keys.discard(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.keys


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)