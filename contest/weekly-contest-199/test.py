

class LinkList(object):
    def __init__(self, val):
        self.val = val
        self.next = None

# 1,2,3,4
#         tmp, pre, cur = None, None, head
#         while cur:
#             tmp = cur.next
#             pre, cur.next = cur, pre
#             cur = tmp
#
#         return pre
def reverse_link_list(root):
    pre = None
    cur = root
    while cur.next:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    cur.next = pre
    return cur



if __name__ == '__main__':
    l1 = LinkList(0)
    l2 = LinkList(1)
    l1.next = l2
    test_cases = [l1]
    for i in test_cases:
        res = reverse_link_list(l1)
        print(res.val, res.next)


