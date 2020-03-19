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

        if key in self.items:
            self.items.pop(key)
        else:

            if self.remain > 0:
                self.remain -= 1
            else:
                self.items.popitem(last=False)

        self.items[key] = value