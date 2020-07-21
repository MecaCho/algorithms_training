'''
437. 路径总和 III
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11


437. Path Sum III
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def sum_count_with_root(root, sum_):
            if not root:
                return 0
            new_sum = sum_ - root.val
            res = 0
            if new_sum == 0:
                res = 1
            return res + sum_count_with_root(root.left, new_sum) + sum_count_with_root(root.right, new_sum)

        def sum_count_without_root(root):
            if not root:
                return 0
            else:
                no_root_l = sum_count_without_root(root.left)
                no_root_r = sum_count_without_root(root.right)
                l = sum_count_with_root(root.left, sum)
                r = sum_count_with_root(root.right, sum)
                return l + r + no_root_l + no_root_r

        return sum_count_without_root(root) + sum_count_with_root(root, sum)



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def sum_count_with_root(root, sum_):
            if not root:
                return 0
            new_sum = sum_ - root.val
            res = 0
            if new_sum == 0:
                res = 1
            return res + sum_count_with_root(root.left, new_sum) + sum_count_with_root(root.right, new_sum)

        def sum_count(root, sum):
            if not root:
                return 0
            else:
                # no_root_l = sum_count_without_root(root.left)
                # no_root_r = sum_count_without_root(root.right)
                # l = sum_count_with_root(root.left, sum)
                # r = sum_count_with_root(root.right, sum)
                # return l + r + no_root_l + no_root_r
                return sum_count(root.left, sum) + sum_count(root.right, sum) + sum_count_with_root(root, sum)

        # return sum_count_without_root(root) + sum_count_with_root(root, sum)
        return sum_count(root, sum)


# golang

'''
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pathSum(root *TreeNode, sum int) int {
	if root == nil{
        return 0
    }
    return pathSum(root.Left, sum) + pathSum(root.Right, sum) + pathSumWithRoot(root, sum)
}

func pathSumWithRoot(root *TreeNode, sum int) int {
    if root == nil{
        return 0
    }
    res := 0
    if root.Val == sum{
        res ++
    }

    return res+pathSumWithRoot(root.Left, sum-root.Val) + pathSumWithRoot(root.Right, sum - root.Val)

}
'''

'''
第一种做法：最容易想到的方法，双递归，先序遍历的变式，把每个遍历到的节点当作root（起点）进行搜索

class Solution {
public:
    int helper(TreeNode* root, int sum) {
        if (root== NULL) return 0;
        sum -= root->val;
        return (sum==0?1:0) + helper(root->left, sum) + helper(root->right, sum);
    }
    int pathSum(TreeNode* root, int sum) {
        if (root == NULL) return 0;
        return helper(root, sum)+pathSum(root->left, sum)+pathSum(root->right, sum);
    }
};
第二种方法，单递归，也是先序遍历的变式，不过搜索方式改变为，把每个遍历到的节点当作终点（路径必须包含终点），记录根到终点的路径，从路径往前搜索
这里需要注意的是：递归栈会保存每次递归的变量，所以可以用一个vector来保存路径，每次递归的过程都取相应的路径，因此递归返回后，要进行弹出。如果这里不理解的话，可以看第三种方法，第三种方法就是第二种方法的非递归形式。

/*class Solution {
public:
    int helper(TreeNode* root, int sum, vector<int>& path) {
        if (root == NULL) return 0;
        path.push_back(root->val);
        int sum_cur = 0;
        int res = 0;
        for (int i= path.size()-1; i>=0; i--) {
            sum_cur+= path[i];
            if (sum_cur == sum) ++res;
        }
        res += helper(root->left, sum, path) + helper(root->right, sum, path);
        path.pop_back();
        return res;
    }
    int pathSum(TreeNode* root, int sum) {
        vector<int> path;
        return helper(root, sum, path);
    }
};*/
第三种方法：先序遍历的非递归方式，本质上就是第二种方法的非递归形式。
用一个pair<TreeNode*, vector<int>> 记录第二种方法中每次递归过程中需要用到的变量。

class Solution {
public:
    int pathSum(TreeNode* root, int sum) {
        if (root == NULL) return 0;
        int res = 0;
        int sum_cur;
        stack<pair<TreeNode*, vector<int> >> m_stack;
        pair<TreeNode*, vector<int> > temp;
        TreeNode* left, *right;
        vector<int> path;
        path.push_back(root->val);
        m_stack.push(make_pair(root, path));
        while (!m_stack.empty()) {
            temp = m_stack.top();
            m_stack.pop();
            sum_cur = 0;
            for (int i = temp.second.size()-1; i>= 0; i--) {
                sum_cur+= temp.second[i];
                if (sum_cur == sum) ++res;
            }
            left = temp.first->left;
            right = temp.first->right;
            if (left!= NULL) {
                temp.second.push_back(left->val);
                m_stack.push(make_pair(left, temp.second));
                temp.second.pop_back();
            }
            if (right!= NULL) {
                temp.second.push_back(right->val);
                m_stack.push(make_pair(right, temp.second));
                temp.second.pop_back();
            }
        }
        return res;
    }
};

'''