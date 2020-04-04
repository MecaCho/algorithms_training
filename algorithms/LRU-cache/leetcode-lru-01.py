import operator

class Values(object):
    def __init__(self, value, last_get, frq, key):
        self.value = value
        self.key = key
        self.last_get = last_get
        self.frq = frq


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.values = {}
        self.time_ = 0
        self.remain = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.time_ += 1
        if key not in self.values:
            return -1
        else:
            value = self.values[key]
            value.frq += 1
            value.last_get = self.time_
            self.values[key] = value
            return self.values[key].value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.time_ += 1
        v = Values(value, self.time_, 1, key)
        if key in self.values:
            v = self.values.pop(key)
            v.value = value
            v.frq += 1
        else:
            if self.remain <= 0:
                if not self.values:
                    return
                values = sorted(self.values.values(), key=operator.attrgetter("frq", "last_get"))
                self.values.pop(values[0].key)
            else:
                self.remain -= 1
        self.values[key] = v


        # Your LFUCache object will be instantiated and called as such:
        # obj = LFUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)



if __name__ == '__main__':
    demo = LFUCache(2)
    ops = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]

    nums = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
    # ress = [None,None,None,None,None,-1,None,19,17,None,-1,None,None,None,-1,None,-1,5,-1,12,None,None,3,5,5,None,None,1,None,-1,None,30,5,30,None,None,None,-1,None,-1,24,None,None,18,None,None,None,None,14,None,None,18,None,None,11,None,None,None,None,None,18,None,None,-1,None,4,29,30,None,12,11,None,None,None,None,29,None,None,None,None,17,-1,18,None,None,None,-1,None,None,None,20,None,None,None,29,18,18,None,None,None,None,20,None,None,None,None,None,None,None]
    ress = [None,None,None,None,None,-1,None,19,-1,None,-1,None,None,None,-1,None,-1,-1,-1,12,None,None,3,-1,-1,None,None,1,None,-1,None,-1,-1,-1,None,None,None,-1,None,-1,-1,None,None,-1,None,None,None,None,-1,None,None,-1,None,None,-1,None,None,None,None,None,-1,None,None,-1,None,-1,29,-1,None,-1,-1,None,None,None,None,-1,None,None,None,None,-1,-1,-1,None,None,None,-1,None,None,None,-1,None,None,None,-1,-1,-1,None,None,None,None,-1,None,None,None,None,None,None,None]
    for i in range(len(ops)):
        op = ops[i]
        num = nums[i]
        res = None
        if op == "put":
            res = demo.put(num[0], num[1])
            print("put", num)
        elif op =="get":
            res = demo.get(num[0])
            print("get", num)
        # print(res)
        if res != ress[i]:
            print(demo.values)
            print(op, num, ress[i],"actual:", res)
            break
