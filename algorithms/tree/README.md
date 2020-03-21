# red-black-tree


• 红黑树是一种近似平衡的二叉查找树，它能够确保任何一个节点的左右子树的高度差不会超过较者中较低那个的1陪。具体来说，红黑树是满足如下条件的二叉查找树(binary search tree):
• 每个节点要么是红色，要么是黑色。
• 根节点必须是黑色
• 红色节点不能连续(也即是，红色节点的孩子和父亲都不能是红色)。
• 对于每个节点，从该点至null(树尾端)的任何路径，都含有相同个数的黑色节点。

## 对比

• AVL trees provide faster lookups than Red Black Trees because they are more strictly balanced.
• Red Black Trees provide faster insertion and removal operations than AVL trees as fewer rotations are done due to relatively relaxed balancing.
• AVL trees store balance factors or heights with each node, thus requires storage for an integer per node whereas Red Black Tree requires only 1 bit of information per node.
• Red Black Trees are used in most of the language libraries like map, multimap, multisetin C++ whereas AVL trees are used in databases where faster retrievals are required.


# read

https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree