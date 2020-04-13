# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        jin = 0

        r = res
        while l1 or l2 or jin:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            
            node = ListNode(((value1 + value2 + jin) % 10))

            jin = (value1 + value2 + jin) / 10

            res.next = node
            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return r.next

def stringToListNode(input):
    # Generate list from the input
    import json
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            l1 = stringToListNode(line)
            line = lines.next()
            l2 = stringToListNode(line)
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
