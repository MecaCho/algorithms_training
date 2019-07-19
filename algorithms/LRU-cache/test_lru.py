import collections


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.items = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        v = self.items.pop(key, -1)
        if v != -1:
            self.items[key] = v
        return v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        print "remain: ", self.remain
        print self.items,

        if key in self.items:
            self.items.pop(key)
        else:

            if self.remain > 0:
                self.remain -= 1
            else:
                self.items.popitem(last=True)

        self.items[key] = value
        print self.items

if __name__ == '__main__':

    # Your LRUCache object will be instantiated and called as such:
    capacity = 3
    obj = LRUCache(capacity)
    key = "abc"
    param_1 = obj.get(key)
    print param_1
    value = "123"
    obj.put(key, value)
    obj.put(1, 1)
    obj.put(2, 2)
    obj.put(3, 3)
    print obj.get(key)
