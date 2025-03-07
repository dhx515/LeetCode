class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10 ** 6 + 1
        self.map = [-1] * self.size  # Initialize all values to -1

    def put(self, key, value):
        """
        value will always be non-negative.
        """
        self.map[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key.
        """
        return self.map[key]

    def remove(self, key):
        """
        Removes the mapping of the specified value key
        if this map contains a mapping for the key.
        """
        self.map[key] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)