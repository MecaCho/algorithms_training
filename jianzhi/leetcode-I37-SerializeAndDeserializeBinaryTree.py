'''
面试题37. 序列化二叉树
请实现两个函数，分别用来序列化和反序列化二叉树。

示例:

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
'''

import json
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def deep_trave(root, deepth, res=[]):
            if not root:
                return res
            if res:
                if len(res) < deepth + 1:
                    res.append([root.val])
                else:
                    res[deepth].append(root.val)
            else:
                res = [[root.val]]
            deep_trave(root.left, deepth + 1, res)
            deep_trave(root.right, deepth + 1, res)
            return res
        def deep_trave1(root, res=[]):
            if not root:
                return res.append(None)
            res.append(root.val)
            deep_trave1(root.left, res)
            deep_trave1(root.right, res)
            return res
        val_list = deep_trave1(root, [])
        return json.dumps(val_list)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        val_list = json.loads(data)
        def get_nodes(val_list):
            if not val_list:
                return None
            if val_list[0] is None:
                val_list.remove(val_list[0])
                return None
            node = TreeNode(val_list[0])
            val_list.remove(val_list[0])
            node.left = get_nodes(val_list)
            node.right = get_nodes(val_list)
            return node

        return get_nodes(val_list)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
