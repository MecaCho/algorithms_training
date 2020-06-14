import collections

import heapq

class PriorityQueue():
    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]


def heapq_demo():
    h = [1,9,8,4,1]
    import heapq
    res = heapq.nlargest(3, h)
    res1 = heapq.nsmallest(3, h)
    print(res, res1)


def search(lines, pattern, his=5):
    all_lines = collections.deque(maxlen=his)
    all_lines.popleft()
    all_lines.pop()
    all_lines.append()
    all_lines.appendleft()
    for line in lines:
        if pattern in line:
            yield line, all_lines
        all_lines.append(line)

def fun118():
    from collections import namedtuple
    Students = namedtuple("Student", ["name", "age"])
    s1 = Students("qwq", 20)
    print(s1, s1.name, s1.age)

if __name__ == '__main__':
    collections.defaultdict()
    ordered_dict = collections.OrderedDict()
    ordered_dict.pop()
    ordered_dict.popitem()
    ordered_dict.get()

    l = [1,2,3,4,1,4,5,6,1,2,3,4,5,6,7]
    d = collections.Counter(l)
    print(d)
    heapq_demo()
    # with open("test.txt") as f:
    #     res = search(f, "test", 5)
    #     for line in res:
    #         print(line)
