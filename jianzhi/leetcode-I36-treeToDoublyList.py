'''
面试题36. 二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。



为了让您更好地理解问题，以下面的二叉搜索树为例：







我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。







特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。



注意：本题与主站 426 题相同：https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

注意：此题对比原题有改动。
'''




"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def dfs(cur):
            if not cur: return
            dfs(cur.left) # 递归左子树
            if self.pre: # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else: # 记录头节点
                self.head = cur
            self.pre = cur # 保存 cur
            dfs(cur.right) # 递归右子树

        if not root:
            return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head



        # if not root:
        #     return
        # node = Node(root.val)
        # if not root.left and not root.right:
        #     node.left = node
        #     node.right = node
        #     return node
        # if not root.left:
        #     right_node = self.treeToDoublyList(root.right)


        #     node.right = right_node
        #     node.left = right_node.left

        #     # right_node.left.right = node
        #     # right_node.left = node

        #     return node
        # if not root.right:
        #     left_node = self.treeToDoublyList(root.left)
        #     node.left = left_node.left
        #     node.right = left_node
        #     left_node.right = node
        #     return node

        # node = Node(root.val)
        # left_node = self.treeToDoublyList(root.left)
        # head = left_node
        # if left_node and left_node.left:
        #     left_node.left.right = node

        # right_node = self.treeToDoublyList(root.right)
        # right_haed = right_node
        # if right_node and right_node.left:
        #     right_node.left.right = left_node
        # if right_node:
        #     right_node.left = node

        # node.left = left_node
        # node.right = right_node

        # if left_node:
        #     left_node.left = right_haed.left
        # print(node)

        # return head
