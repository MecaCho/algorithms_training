# encoding=utf8


'''
297. Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

297. 二叉树的序列化与反序列化
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import json

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
        # print(val_list)
        # val_list = [1, 2, None, None, 3, 4, None, None, 5, None, None]
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
        
        
# solutions

'''
方法一：深度优先搜索
思路和算法

二叉树的序列化本质上是对其值进行编码，更重要的是对其结构进行编码。可以遍历树来完成上述任务。众所周知，我们一般有两个策略：广度优先搜索和深度优先搜索。

广度优先搜索可以按照层次的顺序从上到下遍历所有的节点
深度优先搜索可以从一个根开始，一直延伸到某个叶，然后回到根，到达另一个分支。根据根节点、左节点和右节点之间的相对顺序，可以进一步将深度优先搜索策略区分为：
先序遍历
中序遍历
后序遍历
这里，我们选择先序遍历的编码方式，我们可以通过这样一个例子简单理解：


1 / 12

我们从根节点 1 开始，序列化字符串是 1,。然后我们跳到根节点 2 的左子树，序列化字符串变成 1,2,。现在从节点 2 开始，我们访问它的左节点 3（1,2,3,None,None,）和右节点 4

(1,2,3,None,None,4,None,None)。None,None, 是用来标记缺少左、右子节点，这就是我们在序列化期间保存树结构的方式。最后，我们回到根节点 1 并访问它的右子树，它恰好是叶节点 5。最后，序列化字符串是 1,2,3,None,None,4,None,None,5,None,None,。

即我们可以先序遍历这颗二叉树，遇到空子树的时候序列化成 None，否则继续递归序列化。那么我们如何反序列化呢？首先我们需要根据 , 把原先的序列分割开来得到先序遍历的元素列表，然后从左向右遍历这个序列：

如果当前的元素为 None，则当前为空树
否则先解析这棵树的左子树，再解析它的右子树
具体请参考下面的代码。

代码

JavaC#C++JavaScriptGolang

type Codec struct{}

func Constructor() (_ Codec) {
    return
}

func (Codec) serialize(root *TreeNode) string {
    sb := &strings.Builder{}
    var dfs func(*TreeNode)
    dfs = func(node *TreeNode) {
        if node == nil {
            sb.WriteString("null,")
            return
        }
        sb.WriteString(strconv.Itoa(node.Val))
        sb.WriteByte(',')
        dfs(node.Left)
        dfs(node.Right)
    }
    dfs(root)
    return sb.String()
}

func (Codec) deserialize(data string) *TreeNode {
    sp := strings.Split(data, ",")
    var build func() *TreeNode
    build = func() *TreeNode {
        if sp[0] == "null" {
            sp = sp[1:]
            return nil
        }
        val, _ := strconv.Atoi(sp[0])
        sp = sp[1:]
        return &TreeNode{val, build(), build()}
    }
    return build()
}
复杂度分析

时间复杂度：在序列化和反序列化函数中，我们只访问每个节点一次，因此时间复杂度为 O(n)O(n)，其中 nn 是节点数，即树的大小。
空间复杂度：在序列化和反序列化函数中，我们递归会使用栈空间，故渐进空间复杂度为 O(n)O(n)。
方法二：括号表示编码 + 递归下降解码
思路和算法

我们也可以这样表示一颗二叉树：

如果当前的树为空，则表示为 X
如果当前的树不为空，则表示为 (<LEFT_SUB_TREE>)CUR_NUM(RIGHT_SUB_TREE)，其中：
<LEFT_SUB_TREE> 是左子树序列化之后的结果
<RIGHT_SUB_TREE> 是右子树序列化之后的结果
CUR_NUM 是当前节点的值
根据这样的定义，我们很好写出序列化的过程，后序遍历这颗二叉树即可，那如何反序列化呢？根据定义，我们可以推导出这样的巴科斯范式（BNF）：


T -> (T) num (T) | X
它的意义是：用 T 代表一棵树序列化之后的结果，| 表示 T 的构成为 (T) num (T) 或者 X，| 左边是对 T 的递归定义，右边规定了递归终止的边界条件。

因为：

T 的定义中，序列中的第一个字符要么是 X，要么是 (，所以这个定义是不含左递归的
当我们开始解析一个字符串的时候，如果开头是 X，我们就知道这一定是解析一个「空树」的结构，如果开头是 (，我们就知道需要解析 (T) num (T) 的结构，因此这里两种开头和两种解析方法一一对应，可以确定这是一个无二义性的文法
我们只需要通过开头的第一个字母是 X 还是 ( 来判断使用哪一种解析方法
所以这个文法是 LL(1) 型文法，如果你不知道什么是 LL(1) 型文法也没有关系，你只需要知道它定义了一种递归的方法来反序列化，也保证了这个方法的正确性——我们可以设计一个递归函数：

这个递归函数传入两个参数，带解析的字符串和当前当解析的位置 ptr，ptr 之前的位置是已经解析的，ptr 和 ptr 后面的字符串是待解析的
如果当前位置为 X 说明解析到了一棵空树，直接返回
否则当前位置一定是 (，对括号内部按照 (T) num (T) 的模式解析
具体请参考下面的代码。

代码

JavaC#C++JavaScriptGolang

type Codec struct{}

func Constructor() (_ Codec) {
    return
}

func (c Codec) serialize(root *TreeNode) string {
    if root == nil {
        return "X"
    }
    left := "(" + c.serialize(root.Left) + ")"
    right := "(" + c.serialize(root.Right) + ")"
    return left + strconv.Itoa(root.Val) + right
}

func (Codec) deserialize(data string) *TreeNode {
    var parse func() *TreeNode
    parse = func() *TreeNode {
        if data[0] == 'X' {
            data = data[1:]
            return nil
        }
        node := &TreeNode{}
        data = data[1:] // 跳过左括号
        node.Left = parse()
        data = data[1:] // 跳过右括号
        i := 0
        for data[i] == '-' || '0' <= data[i] && data[i] <= '9' {
            i++
        }
        node.Val, _ = strconv.Atoi(data[:i])
        data = data[i:]
        data = data[1:] // 跳过左括号
        node.Right = parse()
        data = data[1:] // 跳过右括号
        return node
    }
    return parse()
}
复杂度分析

时间复杂度：序列化时做了一次遍历，渐进时间复杂度为 O(n)O(n)。反序列化时，在解析字符串的时候 ptr 指针对字符串做了一次顺序遍历，字符串长度为 O(n)O(n)，故这里的渐进时间复杂度为 O(n)O(n)。
空间复杂度：考虑递归使用的栈空间的大小，这里栈空间的使用和递归深度有关，递归深度又和二叉树的深度有关，在最差情况下，二叉树退化成一条链，故这里的渐进空间复杂度为 O(n)O(n)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/er-cha-shu-de-xu-lie-hua-yu-fan-xu-lie-hua-by-le-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
