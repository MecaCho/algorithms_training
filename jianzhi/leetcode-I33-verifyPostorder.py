'''
面试题33. 二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。



参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true


提示：

数组长度 <= 1000
'''


class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        def cur(i, j):
            if i >= j:
                return True
            start = i
            end = j - 1
            while i < j and postorder[i] <= postorder[j]:
                i += 1
            mid = i - 1
            while i < j and postorder[i] >= postorder[j]:
                i += 1
            if i != j:
                return False


            # print(start, mid, end)
            return cur(start, mid) and cur(mid +1, end)
        return cur(0, len(postorder ) -1)
