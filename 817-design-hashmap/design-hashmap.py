class MyHashMap(object):

    def __init__(self):
        self.max_key = 10**6
        self.map = [None] * (self.max_key + 1)
        self.pair = {}

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.pair[key] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.pair:
           return self.pair[key]
        else:
            return -1 

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.pair:
            self.pair.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)