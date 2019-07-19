class Node(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.traverse_path = []

    def pre_order(self, root):
        if root:
            self.traverse_path.append(root.val)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def mid_order(self, root):
        if root:
            self.mid_order(root.left)
            self.traverse_path.append(root.val)
            self.mid_order(root.right)

    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            self.traverse_path.append(root.val)


if __name__ == '__main__':
    node_list = []
    for i in xrange(10):
        node = Node(val=i)
        node.left = node_list[i/2]
        node.left = node_list[i/2+1]
        node_list.append(node)

