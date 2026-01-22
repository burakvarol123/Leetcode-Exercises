class MyHashSet(object):

    def __init__(self):
        self.max_key = 10**6
        self.present = [False]*(self.max_key + 1)

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.present[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.present[key] = False
        
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.present[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)